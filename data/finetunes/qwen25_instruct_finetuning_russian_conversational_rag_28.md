# Qwen2.5-Instruct Fine-Tuning + Russian Conversational Speech RAG — часть 28

# 40. Labels и loss

Для conversational SFT часто желательно, чтобы модель обучалась прежде всего генерировать assistant response, а не бессмысленно воспроизводить user message.

Конкретная реализация зависит от trainer.

При использовании готовых SFT-инструментов нужно проверить, поддерживают ли они:

- assistant-only loss;
- completion-only loss;
- правильную обработку chat template.

---
