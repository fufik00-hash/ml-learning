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
