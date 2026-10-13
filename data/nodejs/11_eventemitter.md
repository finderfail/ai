# Node.js: EventEmitter

Многие объекты Node (серверы, потоки, процессы) — наследники `EventEmitter`.

```javascript
const { EventEmitter, once } = require('node:events');

class Orders extends EventEmitter {
  create(order) {
    this.emit('created', order);
  }
}

const orders = new Orders();
orders.on('created', (order) => console.log('новый заказ', order.id));
orders.once('created', () => console.log('сработает один раз'));
orders.on('error', (err) => console.error(err));
orders.create({ id: 1 });

const [payload] = await once(orders, 'created');
```

- Обработчики вызываются **синхронно** в порядке подписки.
- Событие `'error'` без подписчика роняет процесс — всегда подписывайтесь на `error`.
- Отписка: `emitter.off(event, handler)`. Утечка памяти — частая причина предупреждения `MaxListenersExceededWarning`.
- `events.once()` и `events.on()` дают промис и асинхронный итератор для событий.
