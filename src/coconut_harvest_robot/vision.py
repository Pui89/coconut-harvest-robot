from __future__ import annotations

import torch
import torch.nn as nn


class TreeVisionEncoder(nn.Module):
    def __init__(self, in_channels: int = 3, hidden_dim: int = 32, out_dim: int = 16):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(in_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
        )
        self.head = nn.Conv2d(hidden_dim, out_dim, kernel_size=1)

    def forward(self, rgb: torch.Tensor) -> torch.Tensor:
        features = self.backbone(rgb)
        return self.head(features)
