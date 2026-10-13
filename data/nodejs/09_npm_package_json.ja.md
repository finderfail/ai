# Node.js：npm と package.json

```bash
npm init -y
npm install express            # 依存関係
npm install -D eslint          # 開発用の依存関係
npm ci                         # lock ファイル通りのクリーンインストール（CI、Docker）
npm update
npm outdated
npm audit
npx some-cli                   # グローバルに入れずにパッケージを実行
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

- **SemVer**：`MAJOR.MINOR.PATCH`。`^5.1.0` は 5.x.x を、`~5.1.0` は 5.1.x だけを許可。
- **package-lock.json** は依存ツリー全体の正確なバージョンを固定する。必ずコミットする。
- `node_modules` は git に入れない。
- 他のパッケージマネージャー：pnpm（容量を節約）、yarn。
