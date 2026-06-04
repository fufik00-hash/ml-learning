from __future__ import annotations

import numpy as np


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    if a.ndim != 1 or b.ndim != 1:
        raise ValueError("dot_product expects 1D vectors")
    if a.shape[0] != b.shape[0]:
        raise ValueError("vectors must have the same length")
    return float(np.sum(a * b))


def matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("matmul expects 2D matrices")
    if A.shape[1] != B.shape[0]:
        raise ValueError("inner dimensions must match")
    return A @ B


def linear_layer(X: np.ndarray, W: np.ndarray, b: np.ndarray) -> np.ndarray:
    if X.ndim != 2:
        raise ValueError("X must be a 2D matrix")
    if W.ndim != 2:
        raise ValueError("W must be a 2D matrix")
    if b.ndim != 1:
        raise ValueError("b must be a 1D vector")
    if X.shape[1] != W.shape[0]:
        raise ValueError("X features must match W input dimension")
    if W.shape[1] != b.shape[0]:
        raise ValueError("W output dimension must match b size")
    return X @ W + b


def main() -> None:
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("dot_product:", dot_product(a, b))

    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    print("matmul:")
    print(matmul(A, B))

    X = np.random.randn(32, 784)
    W = np.random.randn(784, 10)
    bias = np.random.randn(10)
    Y = linear_layer(X, W, bias)
    print("linear_layer output shape:", Y.shape)


if __name__ == "__main__":
    main()
