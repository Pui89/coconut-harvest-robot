from __future__ import annotations

import torch
import torch.nn as nn


class HarvestActionModel(nn.Module):
    def __init__(self, in_dim: int = 32, action_dim: int = 8):
        super().__init__()
        self.net = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(in_dim, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        return self.net(features)
