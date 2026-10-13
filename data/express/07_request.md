# Express.js: объект запроса (req)

```javascript
app.post('/upload/:id', (req, res) => {
  req.params.id;
  req.query.sort;
  req.body;
  req.method;
  req.path;
  req.originalUrl;
  req.get('Authorization');
  req.headers['user-agent'];
  req.ip;
  req.protocol;
  req.hostname;
  req.cookies;
  req.is('application/json');
  req.accepts(['json', 'html']);
});
```

- `req.ip`, `req.protocol` и `req.hostname` за обратным прокси (nginx, Caddy, Cloudflare) будут неверными, пока не включено `app.set('trust proxy', 1)`.
- `req.cookies` появляется только с middleware `cookie-parser`.
- В Express 5 `req.query` — геттер только для чтения: нельзя присвоить ему новый объект; результат валидации храните в отдельном поле, например `req.validated`.
- `req.body` не доверяйте: всегда валидируйте его на сервере.
