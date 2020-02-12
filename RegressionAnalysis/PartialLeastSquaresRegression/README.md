# PLSR ｜ 偏最小二乘法

Table of Contents
=================

   * [PLSR ｜ 偏最小二乘法](#plsr--偏最小二乘法)
      * [sklearn库中的PLS](#sklearn库中的pls)

------

$$
X = TP^T+R\\
Y=UC^T+E= TbC^T+E
$$

- 自变量矩阵
  - 得分T
  - 载荷P
  - 残差矩阵R
- 函数矩阵
  - 得分U
  - 载荷C
  - 误差矩阵E

## sklearn库中的PLS

- pls对象属性
  - **x_weights_** : X的权重 W
  - **x_loadings_** : X的载荷 P
  - **x_scores_** : X矩阵得分 T
  - **y_weights_** : Y的权重
  - **y_loadings_** : Y的载荷.
  - **y_scores_** : Y得分.
  - **coef_** : 回归系数，直接对应于模型: Y = X coef_ + Err
- **划分训练集和测试集**：`X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)`
  - 0.1代表取10%的样本用于预测