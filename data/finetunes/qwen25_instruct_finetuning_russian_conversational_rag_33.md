# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 33

# 47. Пример пайплайна

```text
Raw conversations
       ↓
Удаление мусора
       ↓
Удаление PII
       ↓
Deduplication
       ↓
Style filtering
       ↓
Train / validation split
       ↓
Chat formatting
       ↓
SFT / LoRA / QLoRA
       ↓
Evaluation
       ↓
RAG integration
       ↓
Final evaluation
```

---

# 48. Что делать с пользовательскими сообщениями

Если dataset собирается из реальных диалогов, нужно отдельно продумать приватность.

Удаляй или маскируй:

- имена;
- телефоны;
- адреса;
- email;
- токены;
- API keys;
- номера карт;
- пароли;
- приватные ссылки;
- другие идентификаторы.

Не нужно обучать модель на секретах пользователей.

---

# 49. Data contamination

Следи за тем, чтобы benchmark не попадал в training dataset.

Если тестовый вопрос был в train, результат оценки будет завышен.

Для реальной проверки нужны unseen prompts.

---
