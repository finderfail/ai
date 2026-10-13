# Git: история и различия

```bash
git log --oneline              # краткая история
git log --oneline --graph --all    # граф всех веток
git log -p file.py             # история изменений файла
git log --author="Ilya" --since="2 weeks ago"
git show HEAD                  # последний коммит с изменениями
git show abc1234:path/file.py  # файл в состоянии на коммит

git diff                       # изменения, ещё не добавленные в индекс
git diff --staged              # что войдёт в следующий коммит
git diff main..feature         # разница между ветками
git blame file.py              # кто и когда менял каждую строку
```
