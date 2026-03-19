#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
上夸克/下夸克质量计算（10次运行统计）
用法：python quark_masses.py
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

# 复用 electron_mass.py 中的狄拉克算子构造代码，略写（实际需包含完整函数）
# 为简洁，这里只给出主逻辑框架，实际使用时需复制 electron_mass.py 中的狄拉克构造函数

def quark_mass_range(N, sigma_target, kappa=0.744, seeds=range(1,11)):
    masses = []
    for seed in seeds:
        # 调用狄拉克算子求解函数（需实现）
        lam = compute_dirac_eigenvalue(N, sigma_target, seed)  # 需定义
        if lam is not None:
            masses.append(np.sqrt(lam)*kappa)
    if masses:
        return np.mean(masses), np.std(masses)
    else:
        return None, None

# 实际代码需包含完整的狄拉克算子构造函数，这里省略以节省篇幅。
