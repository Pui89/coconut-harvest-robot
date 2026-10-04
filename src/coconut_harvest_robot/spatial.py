from __future__ import annotations

import torch
import torch.nn as nn


class SpatialFeatureExtractor(nn.Module):
    def __init__(self, in_channels: int = 4, hidden_dim: int = 32, out_dim: int = 16):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(in_channels, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim, kernel_size=3, padding=1),
            nn.ReLU(),
        )
        self.head = nn.Conv2d(hidden_dim, out_dim, kernel_size=1)

    def forward(self, rgb: torch.Tensor, depth: torch.Tensor) -> torch.Tensor:
        stacked = torch.cat([rgb, depth], dim=1)
        features = self.backbone(stacked)
        return self.head(features)
