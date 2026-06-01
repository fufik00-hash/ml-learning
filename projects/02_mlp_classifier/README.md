# Project 02 — MLP Classifier from Scratch

## Цель

Реализовать простую нейросеть без PyTorch и понять forward/backward pass.

## Архитектура

```text
Input -> Linear -> ReLU -> Linear -> Softmax
```

## Dataset

Рекомендуется использовать:

```python
sklearn.datasets.make_moons
```

## Acceptance criteria

- модель обучается;
- accuracy > 85% на toy dataset;
- есть README с объяснением архитектуры;
- есть график loss или текстовый лог обучения.
