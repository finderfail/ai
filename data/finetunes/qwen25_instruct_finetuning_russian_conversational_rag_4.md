# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 4

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Что такое LoRA?"
    },
    {
      "role": "assistant",
      "content": "LoRA — это способ дообучения модели..."
    }
  ]
}
```

Для multi-turn:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Я хочу дообучить Qwen."
    },
    {
      "role": "assistant",
      "content": "Тогда сначала определись, что именно хочешь изменить."
    },
    {
      "role": "user",
      "content": "Именно стиль общения."
    },
    {
      "role": "assistant",
      "content": "Тогда тебе нужен датасет, где главным сигналом будет манера общения..."
    }
  ]
}
```

Главный принцип: качество целевого ответа важнее количества строк.

---
