# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 7

# 5. Chat template и Qwen2.5-Instruct

Instruct-модель ожидает определённую структуру диалога.

При использовании Transformers желательно использовать chat template самой модели, а не вручную придумывать специальные токены.

Концептуально:

```python
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=False
)
```

Точный способ зависит от используемого training framework.

Важно проверять template именно той версии модели, которую ты используешь.

Не следует смешивать разные шаблоны ролей без необходимости.

Стандартные роли:

- `system`
- `user`
- `assistant`

---
