from dataclasses import dataclass


@dataclass(frozen=True)
class RobotConfig:
    image_size: tuple[int, int] = (128, 128)
    hidden_dim: int = 32
    spatial_dim: int = 16
    action_dim: int = 8
    max_height_m: float = 12.0
