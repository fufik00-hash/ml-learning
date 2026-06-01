# Лекция 02 — NumPy и линейная алгебра для нейросетей

## Цель

Понять, как данные и параметры представлены в виде массивов, векторов, матриц и тензоров.

## 1. Scalar, vector, matrix, tensor

```text
scalar: одно число
vector: одномерный массив
matrix: двумерный массив
tensor: многомерный массив
```

Примеры shapes:

```text
()        scalar
(3,)      vector
(2, 3)    matrix
(32, 3, 224, 224) batch of images
```

## 2. Shape

Shape — это размерность массива. В ML shape errors — один из главных источников багов.

Пример:

```text
X: (100, 3)
w: (3, 1)
y = X @ w -> (100, 1)
```

## 3. Matrix multiplication

Матричное умножение используется в Linear layer:

```text
Y = XW + b
```

Где:

```text
X: batch inputs
W: weights
b: bias
Y: outputs
```

## 4. Broadcasting

Broadcasting позволяет NumPy расширять размеры автоматически.

Пример:

```text
X shape: (100, 3)
b shape: (3,)
X + b -> (100, 3)
```

## 5. Почему NumPy важен перед PyTorch

PyTorch Tensor концептуально очень похож на NumPy ndarray, но умеет считать градиенты и работать на GPU.

## Практика

Создай `notebooks/01_numpy_basics.ipynb` или `projects/00_numpy_basics/main.py`.

Задачи:

1. создать `X` формы `(100, 3)`;
2. создать `w` формы `(3, 1)`;
3. создать `b` формы `(1,)`;
4. посчитать `y = X @ w + b`;
5. проверить shape результата;
6. реализовать dot product без NumPy;
7. реализовать matrix multiplication без NumPy.

## Мини-тест

1. Что означает shape `(32, 10)`?
2. Чем `*` отличается от `@` в NumPy?
3. Что такое broadcasting?
4. Почему shape bugs опасны?
5. Какой shape будет у `X @ w`, если `X=(100, 3)`, `w=(3, 1)`?
