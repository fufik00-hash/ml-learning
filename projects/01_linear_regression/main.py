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
