# REST API: коды ответа HTTP

**2xx — успех**
- 200 OK — успешный GET, PUT, PATCH.
- 201 Created — ресурс создан (POST), адрес в `Location`.
- 202 Accepted — принято в асинхронную обработку.
- 204 No Content — успех без тела (часто DELETE).

**3xx — перенаправление**
- 301/308 — постоянный редирект, 302/307 — временный, 304 Not Modified — кеш актуален.

**4xx — ошибка клиента**
- 400 Bad Request — некорректный запрос.
- 401 Unauthorized — нет аутентификации или токен неверный.
- 403 Forbidden — аутентифицирован, но нет прав.
- 404 Not Found — ресурса нет.
- 405 Method Not Allowed — метод не поддерживается для этого URL.
- 409 Conflict — конфликт состояния (дубликат, версия).
- 415 Unsupported Media Type — неверный Content-Type.
- 422 Unprocessable Content — данные не проходят бизнес-проверку.
- 429 Too Many Requests — превышен лимит, см. `Retry-After`.

**5xx — ошибка сервера**
- 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout.
