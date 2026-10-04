from __future__ import annotations

import torch


def normalize_depth(depth: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    depth = depth.clamp_min(eps)
    return depth / depth.max().clamp_min(eps)
