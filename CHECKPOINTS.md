# Checkpoints

## Формат checkpoint

Каждый checkpoint должен содержать:

```markdown
# Checkpoint N

## Что изучено

- ...

## Что реализовано

- ...

## Какие тесты пройдены

- ...

## Какие ошибки были

- ...

## Что нужно повторить

- ...

## Следующий шаг

- ...
```

## Commit message format

```bash
git commit -m "checkpoint-00: initialize learning repository"
git commit -m "checkpoint-01: python and numpy basics"
git commit -m "checkpoint-02: linear regression from scratch"
git commit -m "checkpoint-03: mlp from scratch"
git commit -m "checkpoint-04: pytorch training loop"
git commit -m "checkpoint-05: rag pipeline"
git commit -m "checkpoint-06: ai agent with tools"
```

## Acceptance criteria

Checkpoint считается принятым, если:

- код запускается;
- тесты проходят;
- README обновлён;
- ошибки записаны в `docs/mistakes.md`;
- результаты экспериментов записаны в `docs/experiments.md`;
- можно объяснить решение своими словами.
