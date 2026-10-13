# Git: перенести отдельный коммит — cherry-pick

```bash
git switch release
git cherry-pick abc1234             # применить коммит abc1234 к текущей ветке
git cherry-pick abc1234 def5678     # несколько коммитов
git cherry-pick A^..B               # диапазон от A до B включительно
git cherry-pick --continue          # после решения конфликта
git cherry-pick --abort
```

Удобно, чтобы перенести исправление бага из main в ветку релиза, не сливая всю ветку. Перенесённый коммит получает новый хеш.
