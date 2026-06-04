import numpy as np
import pytest

from projects.numpy_basics.main import dot_product, linear_layer, matmul


def test_dot_product():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    assert dot_product(a, b) == 32.0


def test_dot_product_rejects_non_1d_input():
    a = np.array([[1, 2, 3]])
    b = np.array([4, 5, 6])

    with pytest.raises(ValueError):
        dot_product(a, b)


def test_dot_product_rejects_different_lengths():
    a = np.array([1, 2])
    b = np.array([1, 2, 3])

    with pytest.raises(ValueError):
        dot_product(a, b)


def test_matmul():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])

    expected = np.array([[58, 64], [139, 154]])

    np.testing.assert_array_equal(matmul(A, B), expected)


def test_matmul_rejects_invalid_shapes():
    A = np.ones((100, 3))
    B = np.ones((1, 3))

    with pytest.raises(ValueError):
        matmul(A, B)


def test_linear_layer_output_shape():
    X = np.ones((32, 784))
    W = np.ones((784, 10))
    b = np.ones((10,))

    Y = linear_layer(X, W, b)

    assert Y.shape == (32, 10)


def test_linear_layer_rejects_invalid_bias_shape():
    X = np.ones((32, 784))
    W = np.ones((784, 10))
    b = np.ones((1, 10))

    with pytest.raises(ValueError):
        linear_layer(X, W, b)

