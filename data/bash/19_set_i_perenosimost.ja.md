# Bash：bash・sh・zsh の違いと注意点

- `#!/bin/sh` は POSIX シェル：`[[ ]]`、配列、`{1..5}` は使えません（`$((...))` は使えます）。Ubuntu の `sh` は dash です。
- `#!/usr/bin/env bash` は拡張機能付きの bash。bash で書くならこちらを使います。
- macOS の既定シェルは zsh で、標準の bash は古い 3.2 です（連想配列や `${var,,}` がない）。新しい版は `brew install bash` で入れます。
- ユーティリティにも違いがあります：GNU（Linux）と BSD（macOS）の `sed`、`date`、`grep` はフラグが異なります。たとえば `date -d` は GNU にしかありません。

スクリプトのエラーチェックには `shellcheck script.sh` が役立ちます。
