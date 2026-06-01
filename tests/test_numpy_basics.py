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
