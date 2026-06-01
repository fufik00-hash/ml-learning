# Лекция 01 — Python для ML-инженерии

## Цель

Научиться писать Python-код, который можно тестировать, расширять и использовать в ML-проектах.

## 1. Почему Python доминирует в ML

Python удобен потому, что вокруг него построены основные библиотеки:

- NumPy;
- pandas;
- scikit-learn;
- PyTorch;
- TensorFlow;
- FastAPI;
- Jupyter.

## 2. Функции

Функция должна делать одну вещь и иметь понятный контракт.

```python
def mean_squared_error(y_pred, y_true):
    return ((y_pred - y_true) ** 2).mean()
```

## 3. Type hints

Type hints помогают читать код и находить ошибки раньше.

```python
def add(a: float, b: float) -> float:
    return a + b
```

## 4. Dataclass для конфигов

ML-код часто содержит гиперпараметры. Их удобно хранить в dataclass.

```python
from dataclasses import dataclass

@dataclass
class TrainConfig:
    learning_rate: float = 0.01
    epochs: int = 100
    batch_size: int = 32
```

## 5. Exceptions

Ошибки должны быть явными.

```python
if learning_rate <= 0:
    raise ValueError("learning_rate must be positive")
```

## 6. Модули

Плохой стиль — держать весь код в одном файле. Лучше разделять:

```text
src/training/config.py
src/training/trainer.py
src/models/mlp.py
scripts/train.py
```

## 7. Pytest

Тесты нужны не только для production-кода. В ML они проверяют:

- shapes;
- корректность loss;
- отсутствие NaN;
- воспроизводимость;
- правильность preprocessing.

## Практика

Создай `src/training/config.py` с dataclass `TrainConfig`.

Требования:

- `learning_rate > 0`;
- `epochs > 0`;
- `batch_size > 0`;
- при неправильных значениях выбрасывать `ValueError`.

## Мини-тест

1. Зачем нужен virtual environment?
2. Что такое type hint?
3. Почему ML-код нужно тестировать?
4. Почему конфиги лучше отделять от training loop?
5. Что должен проверять `ValueError` в конфиге обучения?
