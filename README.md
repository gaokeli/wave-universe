# 波宇宙理论数值验证代码

本仓库包含波宇宙理论系列论文中所有核心数值计算的 Python 代码。所有结果均可复现。

## 环境要求
- Python 3.8+
- numpy
- scipy

安装依赖：
```bash
pip install numpy scipy

文件说明

· electron_mass.py：电子质量计算（狄拉克算子，N=2000/5000）
· quark_masses.py：上/下夸克质量计算（10次运行统计）
· strong_coupling.py：强相互作用c值（50次独立实验）
· meson_spectrum.py：介子谱验算（标量拉普拉斯 sigma模式）
· control_experiments.py：S¹/S²负控制实验

运行

每个脚本均可独立运行。例如：

```bash
python electron_mass.py
```

引用

如果您使用这些代码，请引用：
髙克立. 波宇宙理论系列论文. 2026.
