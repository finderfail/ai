# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 29

# 41. Пример простого conversational dataset

```jsonl
{"messages":[{"role":"user","content":"что такое rag?"},{"role":"assistant","content":"если коротко — модель получает релевантные куски внешней базы перед тем, как сформировать ответ"}]}
{"messages":[{"role":"user","content":"а qlora?"},{"role":"assistant","content":"это вариант дообучения через lora, где базовую модель держат в квантованном виде, обычно чтобы сильно сэкономить память"}]}
{"messages":[{"role":"user","content":"бля у меня опять oom"},{"role":"assistant","content":"скорее всего просто не влезает по памяти. попробуй уменьшить batch, sequence length или перейти на qlora"}]}
{"messages":[{"role":"user","content":"можешь объяснить без заумных слов?"},{"role":"assistant","content":"да. по сути lora позволяет дообучать маленькую добавку к модели вместо всей модели целиком"}]}
```

---
