# Express.js: загрузка файлов (multer)

Для `multipart/form-data` нужен **multer** (`npm install multer`).

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
  if (!req.file) return res.status(400).json({ error: 'Нужен PNG или JPEG до 5 МБ' });
  res.status(201).json({ file: req.file.filename });
});
```

Безопасность: не используйте исходное имя файла как путь, ограничивайте размер и тип, храните загрузки отдельно от кода или в S3-совместимом хранилище. MIME-тип клиента можно подделать.
