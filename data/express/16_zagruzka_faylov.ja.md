# Express.js：ファイルのアップロード（multer）

`express.json()` は `multipart/form-data` を解析しないため、ファイルには **multer**（`npm install multer`）が必要です。

```javascript
const multer = require('multer');
const path = require('node:path');
const crypto = require('node:crypto');

const upload = multer({
  storage: multer.diskStorage({
    destination: 'uploads/',
    filename: (req, file, cb) => cb(null, crypto.randomUUID() + path.extname(file.originalname))
  }),
  limits: { fileSize: 5 * 1024 * 1024, files: 1 },
  fileFilter: (req, file, cb) => cb(null, ['image/png', 'image/jpeg'].includes(file.mimetype))
});

app.post('/avatar', auth, upload.single('avatar'), (req, res) => {
  if (!req.file) return res.status(400).json({ error: '5MB 以下の PNG か JPEG が必要です' });
  res.status(201).json({ file: req.file.filename });
});
```

セキュリティ：元のファイル名をパスに使わない、サイズと種類を制限する、アップロードはコードの静的フォルダの外かオブジェクトストレージ（S3 互換）に保存する。クライアントの MIME タイプは偽装できるので、重要な場面では内容も確認する。
