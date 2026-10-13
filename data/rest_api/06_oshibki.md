# REST API: формат ошибок (RFC 9457)

Стандарт **Problem Details for HTTP APIs** (RFC 9457, заменил RFC 7807) описывает единый формат ошибок с типом `application/problem+json`:

```json
{
  "type": "https://api.example.com/problems/validation",
  "title": "Validation failed",
  "status": 400,
  "detail": "Поле email имеет неверный формат",
  "instance": "/api/v1/users",
  "errors": [
    { "field": "email", "message": "Неверный формат email" }
  ]
}
```

- `type` — URI, идентифицирующий вид ошибки (может вести на документацию).
- `title` — краткое описание вида ошибки, `detail` — пояснение конкретного случая.
- `status` дублирует HTTP-код.
- Дополнительные поля (`errors`, `traceId`) разрешены.

Правила: одинаковый формат для всех ошибок, понятные сообщения для разработчика клиента, машиночитаемый код, никакого стека и внутренних деталей в 5xx, `traceId` для поиска в логах.
