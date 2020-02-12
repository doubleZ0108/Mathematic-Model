# 神经网络——多变量非线性建

Table of Contents
=================

   * [神经网络——多变量非线性建](#神经网络多变量非线性建)
      * [神经网络](#神经网络)
         * [常见转换函数](#常见转换函数)
         * [网络训练](#网络训练)
         * [误差后向传播](#误差后向传播)
      * [非线性分类问题](#非线性分类问题)
         * [数据预处理](#数据预处理)
         * [样本集处理](#样本集处理)
         * [分类报告](#分类报告)
      * [MLPClassifier神经网络](#mlpclassifier神经网络)
      * [MLPRegressor | 神经网络回归](#mlpregressor--神经网络回归)

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

------

## 非线性分类问题

### 数据预处理

1. 处理到0～1之间

   ```python
   # 训练集
   minx, maxx = Xtrain.min(), Xtrain.max()
   Xtrain -= minx
   Xtrain /= maxx
   # 测试集
   Xtest -= minx
   Xtest /= maxx
   ```

2. 处理到-1～1之间

   ```python
   # 训练集
   aver = Xtrain.mean(axis=0)
   Xtrain -= aver
   Xtemp = np.abs(Xtrain)
   colmax = Xtemp.max(axis=0)
   Xtrain /= colmax		# 除以列最大值
   # 测试集
   Xtest -= aver
   Xtest /= colmax
   ```

- 处理时，记录处理的参数（如均值），预测新数据集时，用记录的参数对数据预处理

- 分类信息正交化

  > 如样本分三类，则类模式表达为
  >
  > 1类：1 0 0
  >
  > 2类：0 1 0
  >
  > 3类：0 0 1

### 样本集处理

```python
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=.1)
```

### 分类报告

- precision精度：正确预测的个数 / 被预测为正集的个数
  $$
  TP/(TP + FP)
  $$

  - TP: true positive
  - FP: false positive

- recall召回率：正确预测的个数 / 预测个数
  $$
  TP / (TP + FN)
  $$

  - FN: false nagative

- F1得分：2 \* 精度 \* 召回率 / （精度 + 召回率）

- FN：预测值为负集，真值为正集的个数

- FP：预测值为正集，真值为负集的个数

<img src="https://upload-images.jianshu.io/upload_images/12014150-bf8b4f2bbe11137e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

------

## MLPClassifier神经网络

```python
from sklearn.neural_network import MLPClassifier clf=MLPClassifier(hidden_layer_sizes=(100,), alpha=1e-5, random_state=1)
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test) #预测得分 
yhat=clf.predict(X_test) # 预测值 
prob=clf.predict_proba(X_test) # 预测概率
```

- `hidden_layer_sizes`: 元组，每一项时一个隐含层的节点数
- `random_state`: 随机数生成器的状态或种子
- `alpha`: 正则化项参数
- `activation`: 激活函数
  - `identity`: $f(x) = x$
  - `logistic`: $f(x)=1/(1+exp(-x))$
  - `tanh`: $f(x)=tanh(x)$
  - `relu`: $f(x) = max(0,x)$
- `solver`: 优化权重的算法
  - `lbfgs`: 拟牛顿法quasi-Newton的优化器（适合小数据）
  - `sgd`: 随机梯度下降（较大数据，几千个样本以上）
  - `adam`: 基于随机梯度的优化器（较大数据，几千个样本以上）
- `learning_rate`: 学习率，用于权重更新，**只有当solver为sgd时使用**
  - `constant`: 由learning_rate_init给定的恒定学习率
  - `invscaling`: 随着t使用power_t的逆标度指数不断降低学习率
    - effective_learning_rate = learning_rate_init / pow(t, power_t)
  - `adaptive`: 只要训练损耗在下降，就保持学习率为learning_rate_init不变，当连续两次不能降低训练损耗或验证分数停止升高至少to1时，将当前学习率厨艺5
- `max_iter`: 最大迭代次数

## MLPRegressor | 神经网络回归

```python
from sklearn.neural_network import MLPRegressor clf=MLPClassifier( hidden_layer_sizes=(100,), alpha=1e-5, random_state=1) # 很多参数
clf.fit(X_train, y_train) yhat=clf.predict(X_test) # 预测值
```

