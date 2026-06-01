# Лекция 05 — PyTorch basics

## Цель

Научиться использовать PyTorch для обучения моделей без ручного вычисления градиентов.

## 1. Tensor

`torch.Tensor` похож на NumPy array, но может:

- работать на GPU;
- хранить computational graph;
- автоматически считать gradients.

## 2. requires_grad

Если `requires_grad=True`, PyTorch отслеживает операции над тензором.

```python
x = torch.tensor(2.0, requires_grad=True)
y = x * x
y.backward()
print(x.grad)
```

## 3. nn.Module

Модель обычно наследуется от `torch.nn.Module`.

```python
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 2),
        )

    def forward(self, x):
        return self.net(x)
```

## 4. Optimizer

Optimizer обновляет параметры.

```python
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
```

## 5. Training loop

Базовый цикл:

```text
for epoch:
    forward
    loss
    backward
    optimizer.step
    optimizer.zero_grad
```

## Практика

Перепиши MLP classifier на PyTorch.

Файлы:

```text
src/models/mlp.py
src/training/trainer.py
scripts/train.py
```

## Мини-тест

1. Чем Tensor отличается от ndarray?
2. Зачем нужен `requires_grad`?
3. Что делает `loss.backward()`?
4. Почему нужно вызывать `optimizer.zero_grad()`?
5. Чем `model.train()` отличается от `model.eval()`?
