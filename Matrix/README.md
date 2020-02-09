# 矩阵类库 | numpy

[TOC]

------

## 创建矩阵

- `A = np.array([[1,2,3],[4,5,6]])`
- 从文件中读取`A = np.loadtxt('data.txt', delimiter=',')`
  - 第二个参数指定分隔符，默认为【空格/tab】
- 预定矩阵
  - 零阵：`A = np.zeros((2,3))`
  - 单位阵：`A = np.eye(5,5n)`
  - `A = np.random.standard_normal((2,3))`

## 保存矩阵

`np.savetxt('_path_.txt', A, fmt='%5.2f', delimiter='\t', newline='\r\t')`

- fmt：数据格式（宽度为5位，保留2位小数）
- delimiter：列分隔符
- newline：换行符

## 基础运算

- 矩阵+，-
- 乘法：C = A.dot(B)
- 乘方：各元素的乘方
- 转置：B = A.T
- 逆：B = np.linalg.inv(A)

## 聚集函数

默认情况对矩阵的所有元素进行

- axis=0时，按列操作
- axis=1时，按行操作

```python
x = np.array([[1,2,3],[4,5,6]])
x.sum()					# 21
x.sum(axis=0)		# [5 7 9]
x.sum(axis=1)		# [6 15]
```

- `sum()`：元素和
- `std()`：方差
- `mean()`：均值

## 其他操作

- `A.round(n)`：每位保留n位小数
- **矩阵合并**
  - `c = np.c_[a,b]`列合并
  - `c = np.r_[a,b]`行合并
- **增加新行或列**：`np.insert()`
- `A.shape`：矩阵的行数和列数
- **矩阵分片**
  - `B = A[:2, 2:]`: 前两行，2～最后所有的列组成的矩阵
- **行(列)互换**
  - 交换行：`A[[0:2],:] = A[[2,0],:]`交换第0行和第2行
  - 交换列：`A[:,[0,2]] = A[:,[2.0]]`交换第0列和第2列

## SVD分解

按特征值由大到小，逐个提取特征向量

`B = np.linalg.svg(A, full_matrices=False)`

- 第二个参数一定要写，否则按照复数分解
- 用于特征提取、降维、数据可视化
- 实矩阵的SVD分解：将一个实矩阵分解为三个矩阵的乘积，A = USV
  - S: 一维矩阵，矩阵A的实特征值由大到小
  - U: 列正交矩阵
  - V: 行正交矩阵