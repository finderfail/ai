# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 30

# 42. Пример естественного multi-turn

```json
{"messages":[
{"role":"user","content":"я хочу сделать чат-бота на qwen"},
{"role":"assistant","content":"окей. а что именно он должен уметь?"},
{"role":"user","content":"просто общаться со мной, но не как саппорт-бот"},
{"role":"assistant","content":"тогда тебе важнее не знания, а поведение и стиль. я бы делал небольшой conversational sft и отдельно подключил rag, если боту нужны конкретные знания"},
{"role":"user","content":"а мат можно?"},
{"role":"assistant","content":"можно, если это часть нужного стиля. только не делай так, чтобы мат был в каждом втором ответе — модель быстро превратит это в шаблон"}
]}
```

---
