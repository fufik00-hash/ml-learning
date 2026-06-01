# Лекция 04 — MLP from scratch

## Цель

Понять, как несколько linear layers и activation functions образуют нейросеть.

## 1. Нейрон

Упрощённо:

```text
output = activation(w1*x1 + w2*x2 + ... + b)
```

## 2. Linear layer

```text
Y = XW + b
```

Где:

- `X` — batch входов;
- `W` — матрица весов;
- `b` — bias;
- `Y` — выход слоя.

## 3. Activation function

Без нелинейностей сеть из нескольких Linear layers эквивалентна одному Linear layer.

Популярные функции:

- ReLU;
- sigmoid;
- tanh;
- GELU.

## 4. MLP

MLP — multilayer perceptron.

Пример:

```text
Input -> Linear -> ReLU -> Linear -> Softmax
```

## 5. Forward pass

Forward pass — вычисление предсказаний.

## 6. Backward pass

Backward pass — вычисление градиентов.

## Практика

Сделай `projects/02_mlp_classifier/`.

Требования:

- toy dataset через `sklearn.datasets.make_moons`;
- MLP без PyTorch;
- ReLU;
- cross-entropy или упрощённый loss;
- accuracy > 85%.

## Мини-тест

1. Почему нужны activation functions?
2. Что делает Linear layer?
3. Что такое forward pass?
4. Что такое backward pass?
5. Почему MLP может решать нелинейные задачи?
