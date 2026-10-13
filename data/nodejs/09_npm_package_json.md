# Node.js: npm и package.json

```bash
npm init -y
npm install express            # зависимость
npm install -D eslint          # dev-зависимость
npm ci                         # чистая установка строго по lock-файлу (CI, Docker)
npm update
npm outdated
npm audit
npx some-cli                   # запуск пакета без глобальной установки
npm run dev
```

```json
{
  "name": "api",
  "version": "1.0.0",
  "type": "module",
  "engines": { "node": ">=20" },
  "scripts": {
    "dev": "node --watch --env-file=.env src/server.js",
    "start": "node src/server.js",
    "test": "node --test"
  },
  "dependencies": { "express": "^5.1.0" }
}
```

- **SemVer**: `MAJOR.MINOR.PATCH`. `^5.1.0` разрешает 5.x.x, `~5.1.0` — только 5.1.x.
- **package-lock.json** фиксирует точные версии всего дерева — обязательно коммитьте его.
- `node_modules` в git не добавляйте.
- Альтернативные менеджеры: pnpm (экономит место), yarn.
