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
