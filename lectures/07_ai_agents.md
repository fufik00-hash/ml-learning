# Лекция 07 — AI Agents

## Цель

Понять, как LLM превращается в агента через инструменты, состояние, планирование и evaluation.

## 1. LLM vs Agent

LLM генерирует текст.

Agent использует LLM как компонент системы, которая может выполнять действия.

## 2. Agent loop

```text
Task -> Plan -> Choose tool -> Execute -> Observe -> Update state -> Continue/Finish
```

## 3. Tools

Инструмент — функция с понятным контрактом.

Примеры:

```text
read_file(path)
write_file(path, content)
search_files(query)
run_python(code)
call_api(url)
```

## 4. Memory

Память бывает:

- short-term memory;
- long-term memory;
- semantic memory;
- episodic memory.

## 5. Planner/Executor

Planner разбивает задачу.
Executor выполняет шаги.
Evaluator проверяет результат.

## 6. Failure modes

Агенты часто ломаются из-за:

- плохого tool schema;
- отсутствия retries;
- невалидных аргументов;
- бесконечных циклов;
- галлюцинаций;
- отсутствия evals.

## Практика

Сделай CLI agent, который умеет:

- читать файл;
- искать по директории;
- создавать отчёт;
- сохранять результат.

Файлы:

```text
src/agents/base_agent.py
src/agents/tools.py
src/agents/planner.py
src/agents/executor.py
src/agents/evaluator.py
```

## Мини-тест

1. Чем агент отличается от LLM?
2. Что такое tool schema?
3. Зачем агенту memory?
4. Что делает planner?
5. Почему агенту нужны evals?
