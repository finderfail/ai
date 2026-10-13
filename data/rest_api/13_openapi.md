# REST API: документация OpenAPI

**OpenAPI** (ранее Swagger) — стандартный машиночитаемый формат описания HTTP API в YAML или JSON. Текущие версии спецификации — 3.0 и 3.1.

```yaml
openapi: 3.1.0
info:
  title: Shop API
  version: 1.0.0
paths:
  /users/{id}:
    get:
      summary: Получить пользователя
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string }
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: '#/components/schemas/User' }
        '404': { description: Not found }
components:
  schemas:
    User:
      type: object
      required: [id, email]
      properties:
        id: { type: string }
        email: { type: string, format: email }
```

Что даёт: интерактивная документация (Swagger UI, Redoc), генерация клиентов и серверных заглушек, валидация запросов, контрактные тесты. Держите спецификацию в репозитории рядом с кодом.
