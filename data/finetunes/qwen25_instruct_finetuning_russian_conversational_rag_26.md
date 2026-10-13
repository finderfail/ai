# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 26

# 36. Epochs

Больше эпох не означает автоматически лучше.

Для небольшого dataset несколько эпох могут быстро привести к overfitting.

Если dataset очень маленький, даже одна-две эпохи могут уже сильно изменить поведение.

Лучше смотреть:

- validation loss;
- ручные ответы;
- повторяемость;
- стиль;
- instruction following.

---

# 37. Batch size и gradient accumulation

Effective batch size приблизительно определяется как:

`per_device_batch_size × gradient_accumulation_steps × количество устройств`

Например:

```text
batch = 2
gradient accumulation = 8
devices = 1

effective batch = 16
```

Gradient accumulation позволяет имитировать больший batch при ограниченной VRAM.

---
