# Лекция 03 — Loss, производные и gradient descent

## Цель

Понять, как модель обучается через минимизацию ошибки.

## 1. Модель как функция

Простейшая модель:

```text
y_pred = wx + b
```

Параметры:

```text
w — weight
b — bias
```

## 2. Loss function

Loss показывает, насколько предсказание отличается от правильного ответа.

Для регрессии часто используется MSE:

```text
MSE = mean((y_pred - y_true)^2)
```

## 3. Производная

Производная показывает, как изменение входа влияет на изменение выхода.

Если loss зависит от параметра `w`, производная показывает, увеличит или уменьшит loss изменение `w`.

## 4. Gradient

Gradient — вектор производных по параметрам.

```text
gradient = [dL/dw, dL/db]
```

## 5. Gradient descent

Обновление параметров:

```text
w = w - learning_rate * dL/dw
b = b - learning_rate * dL/db
```

## 6. Learning rate

Learning rate управляет размером шага.

Если он слишком большой, обучение может расходиться.
Если слишком маленький, обучение будет медленным.

## Практика

Реализуй linear regression from scratch в `projects/01_linear_regression/main.py`.

Минимальные требования:

- генерация synthetic dataset;
- параметры `w`, `b`;
- forward pass;
- MSE loss;
- ручные gradients;
- parameter update;
- вывод loss каждые N эпох.

## Мини-тест

1. Что измеряет loss?
2. Что такое gradient?
3. Почему параметры обновляются со знаком минус?
4. Что произойдёт при слишком большом learning rate?
5. Чем parameter отличается от hyperparameter?
