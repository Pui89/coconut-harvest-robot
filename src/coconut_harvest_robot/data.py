from __future__ import annotations

import numpy as np
import torch


class SyntheticOrchard:
    @staticmethod
    def generate_rgb(height: int = 128, width: int = 128) -> torch.Tensor:
        y, x = np.mgrid[0:height, 0:width]
        base = np.zeros((height, width), dtype=np.float32)
        base += 0.35
        base += 0.25 * np.sin(x / 20.0)
        base += 0.15 * np.cos(y / 25.0)

        canopy_x0, canopy_x1 = 25, 100
        canopy_y0, canopy_y1 = 20, 110
        base[canopy_y0:canopy_y1, canopy_x0:canopy_x1] += 0.7

        coconut_x = [38, 48, 62, 80, 92]
        coconut_y = [42, 60, 46, 58, 66]
        for cx, cy in zip(coconut_x, coconut_y):
            radius = 5
            yy, xx = np.ogrid[:height, :width]
            mask = (xx - cx) ** 2 + (yy - cy) ** 2 <= radius ** 2
            base[mask] = 0.9

        rgb = np.stack([base, 0.6 * np.ones_like(base), 0.4 * np.ones_like(base)], axis=0)
        return torch.tensor(rgb, dtype=torch.float32).unsqueeze(0)

    @staticmethod
    def generate_depth(height: int = 128, width: int = 128) -> torch.Tensor:
        y, x = np.mgrid[0:height, 0:width]
        depth = np.zeros((height, width), dtype=np.float32)
        depth += 0.2
        depth[20:110, 25:100] += 0.7
        for cx, cy in [(38, 42), (48, 60), (62, 46), (80, 58), (92, 66)]:
            yy, xx = np.ogrid[:height, :width]
            mask = (xx - cx) ** 2 + (yy - cy) ** 2 <= 25
            depth[mask] = 1.0
        depth = depth / depth.max()
        return torch.tensor(depth, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
