# ML Learning

Учебный репозиторий для изучения машинного обучения, нейросетей, PyTorch, LLM, RAG и AI agents с нуля.

## Главная цель

Постепенно пройти путь от базового Python и NumPy до собственных tiny/small моделей, RAG-систем и production-like AI agents.

## Как работать с этим репозиторием

Каждый учебный модуль состоит из:

1. лекции;
2. мини-теста;
3. практической задачи;
4. проверки через pytest или checklist;
5. checkpoint-коммита;
6. ревью через ChatGPT.

## Основные директории

```text
lectures/      Конспекты лекций
tests/         Тесты и проверочные вопросы
projects/      Практические проекты
src/           Переиспользуемый код
docs/          Глоссарий, ошибки, эксперименты, промпты
configs/       Конфиги моделей и агентов
scripts/       CLI-скрипты для запуска обучения, RAG и агентов
notebooks/     Jupyter notebooks
```

## Текущий roadmap

См. `ROADMAP.md`.

## Checkpoints

См. `CHECKPOINTS.md`.

## Правило безопасности

Не коммить:

```text
.env
API keys
GitHub tokens
SSH keys
service account keys
private datasets
```

Для секретов используй `.env`, а в репозиторий добавляй только `.env.example`.
