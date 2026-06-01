"""
setup_course_and_push.py

Создаёт стартовый учебный репозиторий по ML, нейросетям, RAG и AI agents,
затем делает git add, git commit и git push.

Как использовать:

1. Склонируй репозиторий:
   git clone https://github.com/fufik00-hash/ml-learning.git
   cd ml-learning

2. Убедись, что GitHub авторизация уже настроена локально:
   gh auth login
   gh auth status

   Либо используй Git Credential Manager / SSH-ключи.

3. Положи этот файл в корень репозитория.

4. Запусти:
   python setup_course_and_push.py

Скрипт безопасен в том смысле, что он НЕ просит токен и НЕ хранит секреты.
Он использует только локальную git-авторизацию, уже настроенную на твоей машине.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from textwrap import dedent


ROOT = Path.cwd()


FILES: dict[str, str] = {
    "README.md": """
# ML Learning

Учебный репозиторий для изучения машинного обучения, нейросетей, PyTorch, LLM, RAG и AI agents с нуля.

## Главная цель

Постепенно пройти путь от базового Python и NumPy до собственных tiny/small моделей, RAG-систем и production-like AI agents.

## Как работать с этим репозиторием

Каждый учебный модуль состоит из:

1. лекции;
2. мини-теста;
3. практической задачи;
4. проверки через pytest или checklist;
5. checkpoint-коммита;
6. ревью через ChatGPT.

## Основные директории

```text
lectures/      Конспекты лекций
tests/         Тесты и проверочные вопросы
projects/      Практические проекты
src/           Переиспользуемый код
docs/          Глоссарий, ошибки, эксперименты, промпты
configs/       Конфиги моделей и агентов
scripts/       CLI-скрипты для запуска обучения, RAG и агентов
notebooks/     Jupyter notebooks
```

## Текущий roadmap

См. `ROADMAP.md`.

## Checkpoints

См. `CHECKPOINTS.md`.

## Правило безопасности

Не коммить:

```text
.env
API keys
GitHub tokens
SSH keys
service account keys
private datasets
```

Для секретов используй `.env`, а в репозиторий добавляй только `.env.example`.
""",

    "ROADMAP.md": """
# Roadmap

## Stage 0 — Foundation

Цель: подготовить базу для ML-инженерии.

Темы:

- Git/GitHub
- Python для ML
- NumPy
- линейная алгебра
- основы производных
- вероятность и статистика
- reproducibility
- pytest

Результат:

- понятна структура ML-проекта;
- есть рабочее окружение;
- есть первые тесты;
- есть первый checkpoint.

---

## Stage 1 — Neural Networks from Scratch

Цель: понять, как работает обучение модели без магии PyTorch.

Темы:

- linear regression;
- loss function;
- gradient descent;
- MLP;
- activation functions;
- backpropagation;
- tiny autograd engine.

Результат:

- реализована линейная регрессия с нуля;
- реализован MLP с нуля;
- реализован маленький autograd engine.

---

## Stage 2 — PyTorch

Цель: перейти от ручных реализаций к production-style training loop.

Темы:

- torch.Tensor;
- autograd;
- nn.Module;
- Dataset;
- DataLoader;
- optimizer;
- train/eval mode;
- checkpoints;
- metrics.

Результат:

- написан reusable Trainer;
- модель обучается через конфиг;
- есть тесты и метрики.

---

## Stage 3 — Architectures

Цель: понять основные архитектуры нейросетей.

Темы:

- MLP;
- CNN;
- RNN/LSTM;
- Attention;
- Transformer.

Результат:

- CNN classifier;
- tiny character-level Transformer;
- понимание attention-механизма.

---

## Stage 4 — LLM Applications

Цель: научиться строить приложения поверх LLM.

Темы:

- tokenization;
- embeddings;
- vector search;
- chunking;
- RAG;
- prompt engineering;
- tool calling;
- structured outputs.

Результат:

- локальный RAG по markdown-файлам;
- промпты для классификации, извлечения данных и суммаризации;
- базовый tool-calling pipeline.

---

## Stage 5 — AI Agents

Цель: собрать agentic system с инструментами, памятью, планированием и оценкой.

Темы:

- agent loop;
- planner/executor;
- tools;
- memory;
- reflection;
- multi-agent workflow;
- evals;
- FastAPI deployment.

Результат:

- CLI agent;
- code review agent;
- production-like agent API;
- набор eval-тестов.
""",

    "CHECKPOINTS.md": """
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
""",

    ".gitignore": """
.venv/
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.env.*
!.env.example
data/*
!data/.gitkeep
checkpoints/
runs/
wandb/
.DS_Store
.pytest_cache/
.mypy_cache/
.ruff_cache/
""",

    ".env.example": """
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4.1-mini
EMBEDDING_MODEL=text-embedding-3-small
""",

    "requirements.txt": """
numpy
pandas
matplotlib
scikit-learn
torch
torchvision
tqdm
jupyter
pytest
pydantic
fastapi
uvicorn
python-dotenv
faiss-cpu
sentence-transformers
openai
""",

    "lectures/00_how_to_learn_ml.md": """
# Лекция 00 — Как не потеряться в ML, нейросетях и AI agents

## Цель

Понять карту области: где заканчивается обычное программирование, где начинается ML, чем нейросеть отличается от LLM-приложения и почему агент — это не просто чат-бот.

## 1. Обычная программа vs ML-модель

Обычная программа работает по явно заданным правилам:

```text
input -> rules written by developer -> output
```

ML-модель обучается на данных:

```text
input + target -> training algorithm -> parameters
new input + learned parameters -> prediction
```

Разница принципиальная: в обычной программе правила пишет человек, а в ML правила частично извлекаются из данных.

## 2. Что такое модель

Модель — это параметризованная функция.

Пример:

```text
y = wx + b
```

Здесь `w` и `b` — параметры. Обучение означает подбор таких параметров, при которых ошибка модели становится меньше.

## 3. Что такое нейросеть

Нейросеть — это композиция слоёв:

```text
Input -> Linear -> Activation -> Linear -> Output
```

Она тоже является функцией, но с большим числом параметров.

## 4. Что такое loss function

Loss function измеряет ошибку модели.

Пример для регрессии:

```text
MSE = mean((prediction - target)^2)
```

Если loss большой, модель ошибается сильно. Если loss уменьшается на train и validation данных, обучение идёт в правильном направлении.

## 5. Что такое gradient descent

Gradient descent — метод изменения параметров в сторону уменьшения ошибки.

Идея:

```text
parameter = parameter - learning_rate * gradient
```

Градиент показывает, как изменение параметра влияет на loss.

## 6. Tiny, small и big models

Условно:

- tiny model — маленькая учебная или embedded-модель;
- small model — модель, которую можно обучать/дообучать на одной GPU или даже CPU для простых задач;
- big model — большая LLM или vision-модель с миллиардами параметров.

В этом курсе сначала строятся tiny-модели, потом small-пайплайны, затем приложения поверх big models.

## 7. Что такое LLM

LLM — большая языковая модель, обученная предсказывать и генерировать текстовые последовательности. Она не равна агенту. LLM — это двигатель рассуждения/генерации, но не вся система.

## 8. Что такое RAG

RAG — Retrieval-Augmented Generation.

Схема:

```text
user question -> retrieve relevant documents -> put context into prompt -> generate answer
```

RAG нужен, когда модель должна отвечать по внешним документам без fine-tuning.

## 9. Что такое AI agent

AI agent — система, которая может:

- принять цель;
- построить план;
- выбрать инструмент;
- выполнить действие;
- обработать результат;
- продолжить или завершить работу.

Базовый цикл:

```text
Goal -> Plan -> Action -> Observation -> Update State -> Finish or Continue
```

## 10. Почему agent eval важнее демо

Агент может выглядеть умным на одном примере, но ломаться на краевых случаях. Поэтому нужны:

- unit tests;
- integration tests;
- golden tasks;
- success rate;
- latency;
- cost tracking;
- regression tests.

## Практика

Создай и проверь файлы:

```text
README.md
ROADMAP.md
CHECKPOINTS.md
docs/glossary.md
docs/experiments.md
docs/mistakes.md
```

## Мини-тест

Ответь письменно:

1. Чем ML-модель отличается от обычной программы?
2. Что такое параметр модели?
3. Что такое loss function?
4. Что такое gradient descent?
5. Чем LLM отличается от AI agent?
6. Когда нужен RAG?
7. Почему нельзя оценивать агента по одному удачному примеру?
""",

    "lectures/01_python_for_ml.md": """
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
""",

    "lectures/02_numpy_linear_algebra.md": """
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
""",

    "lectures/03_gradient_descent.md": """
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
""",

    "lectures/04_neural_network_from_scratch.md": """
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
""",

    "lectures/05_pytorch_basics.md": """
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
""",

    "lectures/06_rag.md": """
# Лекция 06 — RAG: Retrieval-Augmented Generation

## Цель

Понять, как строить систему ответов по документам без fine-tuning модели.

## 1. Проблема LLM

LLM не знает твои локальные документы, если они не переданы в контекст. Также она может ошибаться или галлюцинировать.

## 2. RAG pipeline

```text
Documents -> chunks -> embeddings -> vector store -> retrieval -> prompt -> answer
```

## 3. Chunking

Документы режутся на фрагменты. Плохой chunking ухудшает retrieval.

Параметры:

- chunk size;
- overlap;
- separators;
- metadata.

## 4. Embeddings

Embedding — векторное представление текста. Близкие по смыслу тексты имеют близкие векторы.

## 5. Vector search

По вопросу строится embedding, затем ищутся ближайшие chunks.

## 6. Generation

Найденные chunks добавляются в prompt как context.

## 7. Evaluation

RAG нужно проверять по:

- retrieval quality;
- answer factuality;
- citation correctness;
- hallucination rate;
- latency;
- cost.

## Практика

Сделай локальный RAG по файлам из `docs/`.

Файлы:

```text
src/rag/loader.py
src/rag/chunker.py
src/rag/embeddings.py
src/rag/vector_store.py
src/rag/retriever.py
src/rag/pipeline.py
```

## Мини-тест

1. Чем RAG отличается от fine-tuning?
2. Что такое chunk?
3. Что такое embedding?
4. Что делает vector store?
5. Почему RAG-ответ должен иметь источники?
""",

    "lectures/07_ai_agents.md": """
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
""",

    "tests/theory_test_00.md": """
# Theory Test 00 — ML, LLM, RAG, Agents

Ответь письменно.

Максимум: 30 баллов.
Порог прохождения: 21 балл.

Оценка каждого вопроса:

- 0 — неверно;
- 1 — частично верно;
- 2 — верно;
- 3 — верно и технически хорошо объяснено.

## Вопросы

1. Чем нейросеть отличается от обычной программы?
2. Что такое параметр модели?
3. Что такое loss function?
4. Что такое gradient descent?
5. Чем обучение модели отличается от использования модели?
6. Что такое overfitting?
7. Что такое embedding?
8. Что такое RAG?
9. Чем LLM отличается от AI agent?
10. Почему агента нужно тестировать иначе, чем обычную функцию?
""",

    "tests/theory_test_01_python_numpy.md": """
# Theory Test 01 — Python and NumPy

Максимум: 30 баллов.
Порог прохождения: 21 балл.

## Вопросы

1. Зачем нужен virtual environment?
2. Что такое type hint?
3. Почему ML-код нужно тестировать?
4. Что такое ndarray?
5. Что означает shape `(32, 10)`?
6. Чем matrix multiplication отличается от element-wise multiplication?
7. Что такое broadcasting?
8. Почему нельзя обучать модель на test set?
9. Что такое parameter?
10. Что такое hyperparameter?
""",

    "tests/test_numpy_basics.py": """
import pytest


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    return sum(x * y for x, y in zip(a, b))


def matmul(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Invalid matrix shapes")

    rows = len(A)
    cols = len(B[0])
    inner = len(B)

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = 0
            for k in range(inner):
                value += A[i][k] * B[k][j]
            row.append(value)
        result.append(row)
    return result


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def test_dot_product_shape_error():
    with pytest.raises(ValueError):
        dot_product([1, 2], [1, 2, 3])


def test_matmul():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    assert matmul(A, B) == [[58, 64], [139, 154]]


def test_matmul_shape_error():
    A = [[1, 2]]
    B = [[1, 2]]
    with pytest.raises(ValueError):
        matmul(A, B)
""",

    "src/training/config.py": """
from dataclasses import dataclass


@dataclass
class TrainConfig:
    learning_rate: float = 0.01
    epochs: int = 100
    batch_size: int = 32
    seed: int = 42

    def __post_init__(self) -> None:
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        if self.epochs <= 0:
            raise ValueError("epochs must be positive")
        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive")
""",

    "tests/test_config.py": """
import pytest

from src.training.config import TrainConfig


def test_default_config_is_valid():
    config = TrainConfig()
    assert config.learning_rate == 0.01
    assert config.epochs == 100
    assert config.batch_size == 32


def test_learning_rate_must_be_positive():
    with pytest.raises(ValueError):
        TrainConfig(learning_rate=0)


def test_epochs_must_be_positive():
    with pytest.raises(ValueError):
        TrainConfig(epochs=0)


def test_batch_size_must_be_positive():
    with pytest.raises(ValueError):
        TrainConfig(batch_size=0)
""",

    "projects/01_linear_regression/README.md": """
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
""",

    "projects/01_linear_regression/main.py": """
from __future__ import annotations

import random


def generate_data(n: int = 100, true_w: float = 2.0, true_b: float = 3.0):
    random.seed(42)
    xs = [random.uniform(-10, 10) for _ in range(n)]
    ys = [true_w * x + true_b + random.uniform(-1, 1) for x in xs]
    return xs, ys


def predict(x: float, w: float, b: float) -> float:
    return w * x + b


def mse_loss(y_pred: list[float], y_true: list[float]) -> float:
    return sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / len(y_true)


def train(epochs: int = 500, learning_rate: float = 0.001) -> tuple[float, float]:
    xs, ys = generate_data()

    w = 0.0
    b = 0.0

    for epoch in range(epochs):
        preds = [predict(x, w, b) for x in xs]
        loss = mse_loss(preds, ys)

        d_w = sum(2 * (pred - y) * x for pred, y, x in zip(preds, ys, xs)) / len(xs)
        d_b = sum(2 * (pred - y) for pred, y in zip(preds, ys)) / len(xs)

        w -= learning_rate * d_w
        b -= learning_rate * d_b

        if epoch % 50 == 0:
            print(f"epoch={epoch:04d} loss={loss:.4f} w={w:.4f} b={b:.4f}")

    return w, b


if __name__ == "__main__":
    learned_w, learned_b = train()
    print("Final parameters:")
    print(f"w={learned_w:.4f}")
    print(f"b={learned_b:.4f}")
""",

    "projects/02_mlp_classifier/README.md": """
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
""",

    "projects/03_local_rag/README.md": """
# Project 03 — Local RAG

## Цель

Сделать question-answering систему по локальным markdown-файлам.

## Pipeline

```text
docs -> chunks -> embeddings -> vector search -> context -> answer
```

## Acceptance criteria

- документы загружаются из `docs/`;
- текст режется на chunks;
- есть простой retrieval;
- ответ содержит использованные источники;
- есть тестовые вопросы.
""",

    "projects/04_cli_agent/README.md": """
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
""",

    "src/models/__init__.py": """""",
    "src/training/__init__.py": """""",
    "src/rag/__init__.py": """""",
    "src/agents/__init__.py": """""",

    "docs/glossary.md": """
# Glossary

## ML

Machine Learning — подход, при котором система улучшает качество предсказаний на основе данных.

## Parameter

Обучаемое значение модели, например weight или bias.

## Hyperparameter

Значение, которое задаёт разработчик до обучения: learning rate, batch size, number of layers.

## Loss function

Функция ошибки, которую модель минимизирует во время обучения.

## Gradient

Производная loss по параметрам модели.

## Embedding

Векторное представление объекта: текста, изображения, токена или документа.

## RAG

Retrieval-Augmented Generation — генерация ответа с предварительным извлечением релевантного контекста.

## Agent

Система, которая использует модель, инструменты, память и цикл принятия решений для выполнения задачи.
""",

    "docs/experiments.md": """
# Experiments

Записывай сюда каждый эксперимент.

## Формат

```markdown
## Experiment N — Название

Date:

Goal:

Setup:

Config:

Results:

What worked:

What failed:

Next step:
```
""",

    "docs/mistakes.md": """
# Mistakes

Журнал ошибок. Его цель — ускорять обучение.

## Формат

```markdown
## Mistake N — Краткое название

Context:

Symptom:

Root cause:

Fix:

How to avoid next time:
```
""",

    "docs/prompts.md": """
# Prompts

Сюда сохраняются рабочие промпты для LLM и агентов.

## Prompt template

```text
Role:
Task:
Context:
Constraints:
Output format:
Quality criteria:
```

## Code review prompt

```text
Ты senior Python/ML engineer. Проверь код по критериям:
1. correctness;
2. readability;
3. edge cases;
4. security;
5. tests;
6. refactoring opportunities.
```
""",

    "configs/mlp.yaml": """
model:
  input_dim: 2
  hidden_dim: 32
  output_dim: 2

training:
  learning_rate: 0.001
  epochs: 100
  batch_size: 32
  seed: 42
""",

    "configs/rag.yaml": """
rag:
  docs_dir: docs
  chunk_size: 800
  chunk_overlap: 120
  top_k: 5
""",

    "configs/agent.yaml": """
agent:
  max_steps: 8
  allow_file_write: true
  allow_code_execution: false
""",

    "scripts/train.py": """
def main() -> None:
    print("Training script placeholder. Implement in Stage 2.")


if __name__ == "__main__":
    main()
""",

    "scripts/run_agent.py": """
def main() -> None:
    print("Agent runner placeholder. Implement in Stage 5.")


if __name__ == "__main__":
    main()
""",

    "notebooks/README.md": """
# Notebooks

Здесь будут учебные Jupyter notebooks.

Рекомендуемый порядок:

1. `01_numpy_basics.ipynb`
2. `02_linear_regression_from_scratch.ipynb`
3. `03_mlp_from_scratch.ipynb`
4. `04_pytorch_training_loop.ipynb`
5. `05_embeddings_and_rag.ipynb`
6. `06_agent_with_tools.ipynb`
""",

    "data/.gitkeep": """""",
}


DIRS = [
    "lectures",
    "notebooks",
    "src",
    "src/models",
    "src/training",
    "src/rag",
    "src/agents",
    "tests",
    "projects",
    "projects/01_linear_regression",
    "projects/02_mlp_classifier",
    "projects/03_local_rag",
    "projects/04_cli_agent",
    "docs",
    "configs",
    "scripts",
    "data",
]


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    print(f"$ {' '.join(command)}")
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
    )


def ensure_git_repo() -> None:
    git_dir = ROOT / ".git"
    if not git_dir.exists():
        raise RuntimeError(
            "Текущая директория не является git-репозиторием. "
            "Сначала выполни: git clone https://github.com/fufik00-hash/ml-learning.git && cd ml-learning"
        )


def write_file(relative_path: str, content: str) -> None:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = dedent(content).lstrip("\n")
    path.write_text(normalized, encoding="utf-8")
    print(f"written: {relative_path}")


def create_dirs() -> None:
    for directory in DIRS:
        path = ROOT / directory
        path.mkdir(parents=True, exist_ok=True)
        print(f"dir: {directory}")


def create_files() -> None:
    for relative_path, content in FILES.items():
        write_file(relative_path, content)


def git_commit_and_push() -> None:
    run(["git", "status", "--short"])
    run(["git", "add", "."])

    diff_result = run(["git", "diff", "--cached", "--quiet"], check=False)
    if diff_result.returncode == 0:
        print("Нет изменений для commit.")
        return

    commit_message = "add ml learning lectures tests and checkpoints"
    run(["git", "commit", "-m", commit_message])

    current_branch = run(["git", "branch", "--show-current"])
    branch = current_branch.stdout.strip() or "main"

    push_result = run(["git", "push", "origin", branch], check=False)
    if push_result.returncode != 0:
        print(push_result.stdout)
        print(push_result.stderr)
        raise RuntimeError(
            "git push не выполнен. Проверь локальную GitHub-авторизацию: gh auth status. "
            "Если репозиторий использует другую ветку, выполни push вручную."
        )

    print("Готово: файлы созданы, commit сделан, push выполнен.")


def main() -> None:
    ensure_git_repo()
    create_dirs()
    create_files()
    git_commit_and_push()


if __name__ == "__main__":
    main()
