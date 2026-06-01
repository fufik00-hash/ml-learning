# Project 04 — CLI Agent with Tools

## Цель

Собрать минимального агента, который умеет использовать инструменты.

## Tools

Минимальный набор:

```text
read_file(path)
write_file(path, content)
search_files(query)
summarize_text(text)
```

## Acceptance criteria

Агент должен:

- принять задачу из CLI;
- построить короткий план;
- выбрать инструмент;
- выполнить действие;
- вернуть итоговый ответ;
- обработать хотя бы одну ошибку.
