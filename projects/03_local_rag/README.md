# Project 03 — Local RAG

## Цель

Сделать question-answering систему по локальным markdown-файлам.

## Pipeline

```text
docs -> chunks -> embeddings -> vector search -> context -> answer
```

## Acceptance criteria

- документы загружаются из `docs/`;
- текст режется на chunks;
- есть простой retrieval;
- ответ содержит использованные источники;
- есть тестовые вопросы.
