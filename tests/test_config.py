import pytest

from src.training.config import TrainConfig


def test_default_config_is_valid():
    config = TrainConfig()

    assert config.learning_rate == 0.01
    assert config.epochs == 100
    assert config.batch_size == 32
    assert config.seed == 42
    assert config.validation_split == 0.2
    assert config.log_every == 10


@pytest.mark.parametrize(
    "field,value",
    [
        ("learning_rate", 0),
        ("learning_rate", -0.01),
        ("epochs", 0),
        ("epochs", -1),
        ("batch_size", 0),
        ("batch_size", -1),
        ("seed", -1),
        ("validation_split", 0),
        ("validation_split", 1),
        ("validation_split", -0.1),
        ("validation_split", 1.5),
        ("log_every", 0),
        ("log_every", -1),
    ],
)
def test_invalid_config_values_raise_error(field, value):
    kwargs = {field: value}

    with pytest.raises(ValueError):
        TrainConfig(**kwargs)


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
