# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 8

# 6. Формат датасета

Один из удобных форматов:

```json
{"messages":[{"role":"user","content":"Привет, что такое RAG?"},{"role":"assistant","content":"Если коротко, RAG — это когда модель перед ответом получает релевантные куски внешней базы знаний."}]}
```

JSONL означает, что каждый объект находится на отдельной строке.

Пример:

```jsonl
{"messages":[...]}
{"messages":[...]}
{"messages":[...]}
```

Не нужно делать один огромный JSON-массив, если используемый training pipeline ожидает JSONL.

---
