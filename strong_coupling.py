#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
强相互作用c值计算（50次独立实验）
用法：python strong_coupling.py
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

def compute_c(N=2000, seed=42, radius=0.6):
    # 此函数与之前运行的完全一致
    # 请直接复制您之前成功运行的代码
    pass

if __name__ == "__main__":
    results = []
    for seed in range(1, 51):
        c = compute_c(seed=seed)
        results.append(c)
        print(f"seed {seed}: {c:.6f}")
    results = np.array(results)
    print(f"中位数: {np.median(results):.6f}")
    print(f"平均值: {np.mean(results):.6f} ± {np.std(results):.6f}")
