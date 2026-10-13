# Bash: сеть — curl, ssh, scp

```bash
curl https://example.com                  # GET, вывод на экран
curl -o page.html https://example.com     # сохранить в файл
curl -L URL                               # следовать редиректам
curl -I URL                               # только заголовки
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"test"}' https://api.example.com/items
curl -fsS URL                             # тихо, но с ошибками

ssh user@host                             # подключиться
ssh -i ~/.ssh/key user@host               # с ключом
scp file.txt user@host:/tmp/              # копировать на сервер
scp user@host:/var/log/app.log .          # с сервера
rsync -avz dir/ user@host:/backup/dir/    # синхронизация
ssh-keygen -t ed25519                     # создать ключ
```
