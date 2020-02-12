# 朴素贝叶斯概率建模

Table of Contents
=================

   * [朴素贝叶斯概率建模](#朴素贝叶斯概率建模)
      * [Sklearn库GaussianNB](#sklearn库gaussiannb)

------

NBM - Naive Bayesian Model

**概率模型**：统计事件发生的概率，以大概率对未来进行判断

**贝叶斯推理**：在得出结论时不仅要根据当前所观察的样本信息，还要根据推理者过去的相关经验和知识

**贝叶斯定义**：已知某条件事件的概率，如何得到两事件交换后的概率（已知P(A|B），如何求P(B|A))

- P(A|B）：事件B发生的前提下，事件A发生的概率

$$
P(B|A) = \frac{P(A|B)}{P(B)}
$$

$$
P(类别|特征1,特征2,...,特征n)=\frac{P(特征1|类别)P(特征2|类别)...P(特征n|类别)P(类别)}{P(特征1)P(特征2)...P(特征n)}
$$

<img src="https://upload-images.jianshu.io/upload_images/12014150-365f263bcaf72ca1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:50%;" />

------

## Sklearn库GaussianNB

```python
from sklearn.naive_bayes import GaussianNB 
bayes = GaussianNB()
model=bayes.fit(x, y) #x是特征，y是分类 
pred = model.predict(xNew)
```

| 性别 | 身高(英尺) | 体重(磅) | 脚掌(英寸) |
| ---- | ----- | ----- | ----- |
| **男**   | 6                          | 180                      | 12                         |
| **男**   | 5.92                       | 190                      | 11                         |
| **男**   | 5.58                       | 170                      | 12                         |
| **男**   | 5.92                       | 165                      | 10                         |
| **女**   | 5                          | 100                      | 6                          |
| **女**   | 5.5                        | 150                      | 8                          |
| **女**   | 5.42                       | 130                      | 7                          |