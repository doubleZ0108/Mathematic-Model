# 手写数字识别

[TOC]

------

>  模式识别的关键：手写数字的模式如何表达

- 将每个数字的小图像整理出来
  - 32 \* 32
- 将每个整理的数字小图像转换为一个向量，输入神经网络，训练模型
  - 每2 \* 2的网格中统计黑像素个数，可以得到256个数字，组成向量
- 预测

<img src="https://upload-images.jianshu.io/upload_images/12014150-8e72f87eff790215.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:33%;" />

------

## 图像处理

### 确定阈值

### 去除背景灰度

### 将小数字方块分割出来

实际情况中如果字写的太大 `t = t.resize((32,32), Image.ANTIALIAS)` 调整到32*32

### 标准化

提取出的每个字符图像，大小不一，字符在小图像中位置布局中 希望每个图像大小都是32*32， 且字符的上下、左右边距一样

<img src="https://upload-images.jianshu.io/upload_images/12014150-5b114dce200c5373.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom: 33%;" />

## 数字特征表示

将32\*32的小图像分割成256个 2*2的范围，统计每个2*2的小方框中，像素值为0的个 数，由此将每个字符表达为256个数字组成的向量

## 神经网络

- 输入层：256向量
- 输出层：正交编码
- 中间层：64（注意过拟合）

------

## Sklearn提供的手写数字

sklearn.datasets中有一套手写数字，共有1797个数字图片， 每个图片大小为8*8，以像素点取值为特征，共被分成10类 (10个数字)，可以通过语句:

```python
from sklearn.datasets import load_digits digits = load_digits()
X = digits.data
y = digits.target
```