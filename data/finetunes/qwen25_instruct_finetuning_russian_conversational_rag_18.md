# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 18

# 21. Style transfer vs knowledge training

Если задача:

> «Говори со мной более естественно и менее формально»

это в основном задача поведения/стиля.

Если задача:

> «Знай внутреннюю документацию компании»

это в основном задача RAG.

Если задача:

> «Отвечай по документации компании коротко, разговорно и без канцелярита»

лучше сочетать:

- RAG для знаний;
- fine-tuning для поведения.

---

# 22. Dataset composition

Для conversational fine-tune полезно разделить dataset концептуально:

### A. Общий conversational

Обычные диалоги.

### B. Technical conversational

Технические вопросы с разговорной формой.

### C. Style examples

Примеры желаемой манеры.

### D. Multi-turn

Несколько сообщений в одном контексте.

### E. Negative / contrastive examples

Показывают, какие ответы нежелательны, если используемый training method это поддерживает.

---
