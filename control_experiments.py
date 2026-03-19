#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S¹ 和 S² 上的负控制实验
用法：python control_experiments.py
"""

import numpy as np
from scipy.spatial import KDTree
from scipy.sparse import lil_matrix, diags
from scipy.sparse.linalg import eigsh

def scalar_laplacian_on_sphere(dim, N, radius, seed=42):
    # 直接复制您之前运行的代码
    pass

if __name__ == "__main__":
    kappa = 0.744
    print("S¹ (circle) 最小正特征值:")
    lam1 = scalar_laplacian_on_sphere(1, 1000, 0.5)
    if lam1:
        mass1 = np.sqrt(lam1) * kappa
        print(f"λ = {lam1:.3f}, 质量 = {mass1:.3f} MeV")
