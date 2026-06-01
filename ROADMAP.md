# Roadmap

## Stage 0 — Foundation

Цель: подготовить базу для ML-инженерии.

Темы:

- Git/GitHub
- Python для ML
- NumPy
- линейная алгебра
- основы производных
- вероятность и статистика
- reproducibility
- pytest

Результат:

- понятна структура ML-проекта;
- есть рабочее окружение;
- есть первые тесты;
- есть первый checkpoint.

---

## Stage 1 — Neural Networks from Scratch

Цель: понять, как работает обучение модели без магии PyTorch.

Темы:

- linear regression;
- loss function;
- gradient descent;
- MLP;
- activation functions;
- backpropagation;
- tiny autograd engine.

Результат:

- реализована линейная регрессия с нуля;
- реализован MLP с нуля;
- реализован маленький autograd engine.

---

## Stage 2 — PyTorch

Цель: перейти от ручных реализаций к production-style training loop.

Темы:

- torch.Tensor;
- autograd;
- nn.Module;
- Dataset;
- DataLoader;
- optimizer;
- train/eval mode;
- checkpoints;
- metrics.

Результат:

- написан reusable Trainer;
- модель обучается через конфиг;
- есть тесты и метрики.

---

## Stage 3 — Architectures

Цель: понять основные архитектуры нейросетей.

Темы:

- MLP;
- CNN;
- RNN/LSTM;
- Attention;
- Transformer.

Результат:

- CNN classifier;
- tiny character-level Transformer;
- понимание attention-механизма.

---

## Stage 4 — LLM Applications

Цель: научиться строить приложения поверх LLM.

Темы:

- tokenization;
- embeddings;
- vector search;
- chunking;
- RAG;
- prompt engineering;
- tool calling;
- structured outputs.

Результат:

- локальный RAG по markdown-файлам;
- промпты для классификации, извлечения данных и суммаризации;
- базовый tool-calling pipeline.

---

## Stage 5 — AI Agents

Цель: собрать agentic system с инструментами, памятью, планированием и оценкой.

Темы:

- agent loop;
- planner/executor;
- tools;
- memory;
- reflection;
- multi-agent workflow;
- evals;
- FastAPI deployment.

Результат:

- CLI agent;
- code review agent;
- production-like agent API;
- набор eval-тестов.
