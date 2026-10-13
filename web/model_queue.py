from __future__ import annotations

import os
import threading
import types
from collections import deque
from collections.abc import Iterator

from fastapi.responses import StreamingResponse
from starlette.concurrency import iterate_in_threadpool

CAPACITY = max(1, int(os.getenv("MODEL_CONCURRENCY", "1")))
HEARTBEAT_SECONDS = 2.0


class ModelQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cond = threading.Condition()
        self._waiting: deque[object] = deque()
        self._active = 0

    def join(self) -> object:
        ticket = object()
        with self._cond:
            self._waiting.append(ticket)
            self._cond.notify_all()
        return ticket

    def try_acquire(self, ticket: object) -> bool:
        with self._cond:
            if self._waiting and self._waiting[0] is ticket and self._active < self.capacity:
                self._waiting.popleft()
                self._active += 1
                self._cond.notify_all()
                return True
            return False

    def position(self, ticket: object) -> int:
        with self._cond:
            try:
                return self._waiting.index(ticket) + 1
            except ValueError:
                return 0

    def wait(self, timeout: float) -> None:
        with self._cond:
            self._cond.wait(timeout)

    def leave(self, ticket: object) -> None:
        with self._cond:
            try:
                self._waiting.remove(ticket)
            except ValueError:
                pass
            self._cond.notify_all()

    def release(self) -> None:
        with self._cond:
            self._active = max(0, self._active - 1)
            self._cond.notify_all()

    def stats(self) -> dict:
        with self._cond:
            return {"active": self._active, "waiting": len(self._waiting), "capacity": self.capacity}


model_queue = ModelQueue(CAPACITY)


def needs_model(token_stream) -> bool:
    return isinstance(token_stream, types.GeneratorType)


def queued(token_stream) -> Iterator[tuple[str, object]]:
    if not needs_model(token_stream):
        for token in token_stream:
            yield "token", token
        return

    ticket = model_queue.join()
    acquired = False
    try:
        reported = None
        waited = 0.0
        while not model_queue.try_acquire(ticket):
            position = model_queue.position(ticket)
            if position != reported or waited >= HEARTBEAT_SECONDS:
                yield "queue", position
                reported = position
                waited = 0.0
            model_queue.wait(1.0)
            waited += 1.0
        acquired = True
        if reported is not None:
            yield "start", None
        for token in token_stream:
            yield "token", token
    finally:
        if acquired:
            model_queue.release()
        else:
            model_queue.leave(ticket)
        if isinstance(token_stream, types.GeneratorType):
            token_stream.close()


class ClosingStreamingResponse(StreamingResponse):
    def __init__(self, generator, media_type: str = "text/event-stream"):
        super().__init__(iterate_in_threadpool(generator), media_type=media_type)
        self._generator = generator

    async def __call__(self, scope, receive, send) -> None:
        try:
            await super().__call__(scope, receive, send)
        finally:
            try:
                self._generator.close()
            except ValueError:
                pass


def closing_stream(generator, media_type: str = "text/event-stream") -> StreamingResponse:
    return ClosingStreamingResponse(generator, media_type=media_type)
