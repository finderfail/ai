# Express.js: объект ответа (res)

```javascript
res.status(201).json({ id: 1 });
res.send('текст');
res.sendStatus(204);
res.set('Cache-Control', 'no-store');
res.type('text/plain');
res.location('/users/1');
res.redirect(302, '/login');
res.cookie('sid', token, { httpOnly: true, secure: true, sameSite: 'lax', maxAge: 86400000 });
res.clearCookie('sid');
res.sendFile(path.join(__dirname, 'files', 'report.pdf'));
res.download(filePath, 'report.pdf');
res.format({
  json: () => res.json(data),
  html: () => res.send('<p>...</p>')
});
```

- Ответ можно отправить **только один раз**: после `res.json()` делайте `return`, чтобы код не пошёл дальше.
- `res.json()` сам ставит `Content-Type: application/json`.
- `res.sendFile()` требует абсолютный путь или опцию `root`.
- В Express 5 `res.status()` принимает только целые коды 100–999.
