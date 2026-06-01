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

@pytest.mark.parametrize(
    "dataset_size,batch_size,expected_steps",
    [
        (10_000, 100, 100),
        (10_000, 1_000, 10),
        (1_024, 32, 32),
        (1_000, 128, 8),
        (50_000, 64, 782),
    ],
)
def test_steps_per_epoch(dataset_size, batch_size, expected_steps):
    config = TrainConfig(batch_size=batch_size)

    assert config.steps_per_epoch(dataset_size) == expected_steps


def test_total_steps():
    config = TrainConfig(batch_size=128, epochs=3)

    assert config.total_steps(dataset_size=1_000) == 24


@pytest.mark.parametrize("dataset_size", [0, -1, -100])
def test_steps_per_epoch_requires_positive_dataset_size(dataset_size):
    config = TrainConfig()

    with pytest.raises(ValueError):
        config.steps_per_epoch(dataset_size)
