# Git: работа через pull request (merge request)

1. Обновите main: `git switch main && git pull`.
2. Создайте ветку: `git switch -c feature/short-name`.
3. Коммитьте небольшими шагами, затем `git push -u origin feature/short-name`.
4. Откройте pull request на GitHub/GitLab, опишите что и зачем изменено.
5. Исправляйте замечания ревью новыми коммитами в ту же ветку и пушьте.
6. Если main ушёл вперёд — `git pull --rebase origin main` или `git merge main` в свою ветку.
7. После слияния удалите ветку локально и на сервере.

С GitHub CLI: `gh pr create`, `gh pr status`, `gh pr checkout 123`.
