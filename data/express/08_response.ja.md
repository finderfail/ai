# Express.js：レスポンスオブジェクト（res）

```javascript
res.status(201).json({ id: 1 });
res.send('テキスト');
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

- レスポンスは **1回だけ** 送れる。`res.json()` の後は `return` して処理を進めないようにする。
- `res.json()` は自動で `Content-Type: application/json` を設定する。
- `res.sendFile()` には絶対パスか `root` オプションが必要。
- Express 5 の `res.status()` は 100〜999 の整数コードだけを受け付ける。
