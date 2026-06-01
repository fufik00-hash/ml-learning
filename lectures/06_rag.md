# Лекция 06 — RAG: Retrieval-Augmented Generation

## Цель

Понять, как строить систему ответов по документам без fine-tuning модели.

## 1. Проблема LLM

LLM не знает твои локальные документы, если они не переданы в контекст. Также она может ошибаться или галлюцинировать.

## 2. RAG pipeline

```text
Documents -> chunks -> embeddings -> vector store -> retrieval -> prompt -> answer
```

## 3. Chunking

Документы режутся на фрагменты. Плохой chunking ухудшает retrieval.

Параметры:

- chunk size;
- overlap;
- separators;
- metadata.

## 4. Embeddings

Embedding — векторное представление текста. Близкие по смыслу тексты имеют близкие векторы.

## 5. Vector search

По вопросу строится embedding, затем ищутся ближайшие chunks.

## 6. Generation

Найденные chunks добавляются в prompt как context.

## 7. Evaluation

RAG нужно проверять по:

- retrieval quality;
- answer factuality;
- citation correctness;
- hallucination rate;
- latency;
- cost.

## Практика

Сделай локальный RAG по файлам из `docs/`.

Файлы:

```text
src/rag/loader.py
src/rag/chunker.py
src/rag/embeddings.py
src/rag/vector_store.py
src/rag/retriever.py
src/rag/pipeline.py
```

## Мини-тест

1. Чем RAG отличается от fine-tuning?
2. Что такое chunk?
3. Что такое embedding?
4. Что делает vector store?
5. Почему RAG-ответ должен иметь источники?
