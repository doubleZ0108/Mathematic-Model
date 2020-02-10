# 神经网络——多变量非线性建

[TOC]

------

y = f(x1, x2, ..., xn)，y与xi之间呈非线性

- **线性化**：将对应xi取平方、对数等，以多元线性回归建模

## 神经网络

<img src="https://upload-images.jianshu.io/upload_images/12014150-3825d8a00f3fde7d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

- 每个节点输入：$z_j = \sum x_iw_{ij}$
- 每个节点输出：$h_0 = \frac{1}{1+e^{-z}}$
- 调节$w_{ij}$，使模型收敛

### 常见转换函数

- **sigmoid函数**
  $$
  f(x) = \frac{1}{1+e^{-x}} \\
  f'(x) = f(x)*(1-f(x))
  $$
  

  <img src="https://upload-images.jianshu.io/upload_images/12014150-2e2ee098f29d18f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

  - 用于分类问题：0、1标识两个类别

- **tanh函数**
  $$
  f(x) = tanh(x) \\
  f'(x) = 1.0-tanh(x)**2
  $$
  

  <img src="https://upload-images.jianshu.io/upload_images/12014150-d4e08218a8926cb5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

### 网络训练

- 训练神经网络的过程是<u>调节优化权重的过程</u>
- BP（Back Propagation）
- 由输出层的误差开始，逐步向前层网络修正权重

### 误差后向传播

![image.png](https://upload-images.jianshu.io/upload_images/12014150-1b58e9fc5388d43b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

