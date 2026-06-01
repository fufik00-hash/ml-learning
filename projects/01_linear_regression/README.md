# Project 01 — Linear Regression from Scratch

## Цель

Понять полный цикл обучения модели на простом примере:

```text
y = wx + b
```

## Что нужно реализовать

- synthetic dataset;
- параметры `w` и `b`;
- forward pass;
- MSE loss;
- ручные gradients;
- gradient descent;
- вывод loss;
- финальное сравнение true и learned parameters.

## Критерии готовности

- loss стабильно падает;
- learned `w` и `b` близки к true values;
- код запускается командой:

```bash
python projects/01_linear_regression/main.py
```

## Контрольные вопросы

1. Что такое `w` и `b`?
2. Почему loss уменьшается?
3. Что будет, если learning rate слишком большой?
4. Почему нужно несколько epochs?
