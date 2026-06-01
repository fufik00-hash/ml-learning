from dataclasses import dataclass
from math import ceil


@dataclass
class TrainConfig:
    learning_rate: float = 0.01
    epochs: int = 100
    batch_size: int = 32
    seed: int = 42
    validation_split: float = 0.2
    log_every: int = 10

    def __post_init__(self) -> None:
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        if self.epochs <= 0:
            raise ValueError("epochs must be positive")
        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive")
        if self.seed < 0:
            raise ValueError("seed must be non-negative")
        if not 0 < self.validation_split < 1:
            raise ValueError("validation_split must be between 0 and 1")
        if self.log_every <= 0:
            raise ValueError("log_every must be positive")

    def steps_per_epoch(self, dataset_size: int) -> int:
        if dataset_size <= 0:
            raise ValueError("dataset_size must be positive")
        return ceil(dataset_size / self.batch_size)

    def total_steps(self, dataset_size: int) -> int:
        return self.steps_per_epoch(dataset_size) * self.epochs
