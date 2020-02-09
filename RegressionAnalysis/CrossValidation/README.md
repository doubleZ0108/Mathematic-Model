# 交叉验证

[TOC]

------

建模预报自身，有老王卖瓜之嫌

## 策略

1. 将数据分成n份
2. 将1份从数据集中抽出来作为测试集；剩下的n-1份建模，预测抽取出来的一份
3. 将上述抽取的1份放回，再抽取另一份作为测试集，再进行一次建模预测
4. 循环直到每一份都作为例一次测试集为止
5. 每个样本都被预测了一次且仅一次
6. 将每个样本的真值和预测值之间的误差进行合理的计算，即可对模型的可靠性做出适当的评价

## sklearn库KFold类

`kf = KFold(n_splits=10)`：指定交叉验证的份数n_splits，生成KFold对象，即可完成每一份交叉验证的样本组成

```python
for train_index, test_index in kf.split(X):
  X_train, X_test = X[train_index], X[test_index]
  Y_train, Y_test = Y[train_index], Y[test_index]
```

- X_train，Y_train建模
- X_test预测yhat
- 用yhat和y_test计算预测误差