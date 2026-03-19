#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
电子质量计算（狄拉克算子）
用法：python electron_mass.py
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

def compute_electron_mass(N, seed=42, sigma=0.5):
    """
    计算电子质量（狄拉克算子最小正本征值）
    参数：
        N: 点数（推荐2000或5000）
        seed: 随机种子
        sigma: shift-invert 目标值
    返回：
        电子质量 (MeV)
    """
    radius = 0.6
    kappa = 0.744  # 质量系数
    np.random.seed(seed)

    # 生成S³点集
    pts = np.random.randn(N, 4)
    pts /= np.linalg.norm(pts, axis=1, keepdims=True)

    # 邻接矩阵
    dot_abs = np.abs(pts @ pts.T)
    dot_abs = np.clip(dot_abs, 0, 1)
    dist = 2 * np.arccos(dot_abs)
    A = (dist < radius).astype(int)
    np.fill_diagonal(A, 0)
    neighbors = [np.where(A[i] == 1)[0] for i in range(N)]

    # 狄拉克算子构造
    gamma1 = np.array([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]], dtype=complex)
    gamma2 = np.array([[0,0,0,-1j],[0,0,1j,0],[0,1j,0,0],[-1j,0,0,0]], dtype=complex)
    gamma3 = np.array([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]], dtype=complex)
    gammas = [gamma1, gamma2, gamma3]

    dim = 4 * N
    rows, cols, data = [], [], []
    for i in range(N):
        for a in range(4):
            rows.append(i*4 + a)
            cols.append(i*4 + a)
            data.append(0.0)
        for j in neighbors[i]:
            if j <= i: continue
            vec = pts[j] - pts[i]
            norm = np.linalg.norm(vec)
            if norm < 1e-10: continue
            vec = vec / norm
            coup = np.zeros((4,4), dtype=complex)
            for mu in range(3):
                coup += 1j * gammas[mu] * vec[mu]
            w = 1.0 / norm
            for a in range(4):
                for b in range(4):
                    val = coup[a,b] * w
                    if abs(val) > 1e-10:
                        rows.append(i*4 + a)
                        cols.append(j*4 + b)
                        data.append(val)
                        rows.append(j*4 + b)
                        cols.append(i*4 + a)
                        data.append(np.conj(val))
    L = sp.csr_matrix((data, (rows, cols)), shape=(dim, dim))

    # 求解特征值
    evals, _ = eigsh(L, k=10, sigma=sigma, which='LM', maxiter=10000)
    pos = evals[evals > 1e-10]
    if len(pos) == 0:
        return None
    lam = np.min(pos)
    mass = np.sqrt(lam) * kappa
    return mass

if __name__ == "__main__":
    print("N=2000 电子质量:", compute_electron_mass(2000))
    print("N=5000 电子质量:", compute_electron_mass(5000))
