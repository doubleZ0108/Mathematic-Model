# 手写数字识别

[TOC]

------

## 模式表示

> 模式识别的关键：手写数字的模式如何表达

- 将每个数字的小图像整理出来
  - 32 \* 32
- 将每个整理的数字小图像转换为一个向量，输入神经网络，训练模型
  - 每2 \* 2的网格中统计黑像素个数，可以得到256个数字，组成向量
- 预测

<img src="https://upload-images.jianshu.io/upload_images/12014150-8e72f87eff790215.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:33%;" />

