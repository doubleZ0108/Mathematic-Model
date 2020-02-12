# 数学模型 | Mathematic Model

[TOC]

------

## 关于作者

| 姓名     | 张喆                |
| -------- | ------------------- |
| 学校     | 同济大学            |
| 联系方式 | doubleZ0108@163.com |

## 常见基础数学模型

- **方程**

  - [夹逼法求解一元高次方程]()

- **矩阵**

  - 基础运算
  - SVD分解

- **遗传算法**

  - 数值遗传算法寻优

    > 🌰刹车距离与车速关系

  - 数值遗传算法NGA

- **回归分析**

  - 线性回归
    - 一元线性回归
    - 多元线性回归
  - 降维回归
    - 主成分分析 PCA
    - 主成分回归 PCR
  - 偏最小二乘法 PLSR
  - 交叉验证

- **数据可视化**

  - 常见图表
  - 三维图像
  - 聚类分析
    - 无监督
    - 有监督PLSDA
    - 概率等高线模拟

  > 🌰鸢尾花数据可视化
  >
  > 🌰小麦优、劣颗粒分类聚类可视化

- **神经网络**

  - 神经网络
  - 非线性分类
  - MLPClassifier神经网络
  - MLPRegressor神经网络回归

  > 🌰手写数字图像识别

- **最优化建模**

  - 线性规划

- **深度学习**

  - Keras深度学习模型

- **概率建模**

  - 朴素贝叶斯概率建模 NBM

## 项目结构

```
.
├── DataVisualization
│   ├── Examples
│   │   ├── Iris
│   │   │   ├── IrisClassifyDV.ipynb
│   │   │   ├── IrisContourDV.ipynb
│   │   │   └── IrisDV_3D.ipynb
│   │   ├── README.md
│   │   └── WheatGrainClassification
│   │       ├── WheatGrainClassificationDV.py
│   │       ├── wheat_train_PCA_X.txt
│   │       └── wheat_train_PCA_Y.txt
│   ├── Plot
│   │   ├── plot.py
│   │   ├── plot3d.py
│   │   └── subplot.py
│   └── README.md
├── DeepingLearning
│   ├── Keras
│   │   ├── HandwrittenDigitRecongnition_DL.ipynb
│   │   ├── Wheat
│   │   │   ├── wheat.ipynb
│   │   │   ├── wheat_train_PCA_X.txt
│   │   │   └── wheat_train_PCA_Y.txt
│   │   └── keras_example.ipynb
│   └── README.md
├── Genetic
│   ├── Individual.py
│   └── README.md
├── LinearProgramming
│   ├── Examples
│   │   └── example.py
│   └── README.md
├── Matrix
│   └── README.md
├── NeuralNetwork
│   ├── HandwrittenDigitRecongnition
│   │   ├── HandwrittenDigitRecongnition.ipynb
│   │   ├── HandwrittenDigitRecongnition.py
│   │   ├── README.md
│   │   ├── Sklearn.ipynb
│   │   └── handwritting.png
│   ├── MLPClassifier.ipynb
│   ├── MLPRegressor.ipynb
│   ├── NeuralNetwork.py
│   ├── NeurallNetwork.ipynb
│   ├── README.md
│   └── data
│       ├── 1x0.txt
│       └── 1y0.txt
├── Probability
│   └── NaiveBayesianModel
│       ├── Examples
│       │   ├── Gender
│       │   │   ├── GenderExample.ipynb
│       │   │   └── genderData.txt
│       │   ├── Iris
│       │   │   └── IrisExample.ipynb
│       │   └── NetworkTextAnalysis
│       │       ├── NetworkTextAnalysis.ipynb
│       │       └── text.txt
│       └── README.md
├── README.md
├── RegressionAnalysis
│   ├── CrossValidation
│   │   ├── CrossValidation.py
│   │   └── README.md
│   ├── DimensionReduction
│   │   ├── PrincipleComponentAnalysis
│   │   │   └── PCA.py
│   │   ├── PrincipleComponentRegression
│   │   │   └── PCR.py
│   │   └── README.md
│   ├── PartialLeastSquaresRegression
│   │   ├── PLSR.py
│   │   └── README.md
│   ├── README.md
│   └── UnaryLinearRegression
│       ├── ULR.py
│       └── data.txt
└── SolveEquations
    ├── Algorithms
    │   ├── NumericGeneticAlgorithm.py
    │   ├── OneVarHighOrder.py
    │   └── __pycache__
    ├── Examples
    │   └── Braking Distance Speed
    │       ├── BrakingDistance_Speed.py
    │       └── data.txt
    └── README.md

33 directories, 56 files
(base) jijideMacBook-Pro:tmp doublez$ tree -N
.
├── DataVisualization
│   ├── Examples
│   │   ├── Iris
│   │   │   ├── IrisClassifyDV.ipynb
│   │   │   ├── IrisContourDV.ipynb
│   │   │   └── IrisDV_3D.ipynb
│   │   ├── README.md
│   │   └── WheatGrainClassification
│   │       ├── WheatGrainClassificationDV.py
│   │       ├── wheat_train_PCA_X.txt
│   │       └── wheat_train_PCA_Y.txt
│   ├── Plot
│   │   ├── plot.py
│   │   ├── plot3d.py
│   │   └── subplot.py
│   └── README.md
├── DeepingLearning
│   ├── Keras
│   │   ├── HandwrittenDigitRecongnition_DL.ipynb
│   │   ├── Wheat
│   │   │   ├── wheat.ipynb
│   │   │   ├── wheat_train_PCA_X.txt
│   │   │   └── wheat_train_PCA_Y.txt
│   │   └── keras_example.ipynb
│   └── README.md
├── Genetic
│   ├── Individual.py
│   └── README.md
├── LinearProgramming
│   ├── Examples
│   │   └── example.py
│   └── README.md
├── Matrix
│   └── README.md
├── NeuralNetwork
│   ├── HandwrittenDigitRecongnition
│   │   ├── HandwrittenDigitRecongnition.ipynb
│   │   ├── HandwrittenDigitRecongnition.py
│   │   ├── README.md
│   │   ├── Sklearn.ipynb
│   │   └── handwritting.png
│   ├── MLPClassifier.ipynb
│   ├── MLPRegressor.ipynb
│   ├── NeuralNetwork.py
│   ├── NeurallNetwork.ipynb
│   ├── README.md
│   └── data
│       ├── 1x0.txt
│       └── 1y0.txt
├── Probability
│   └── NaiveBayesianModel
│       ├── Examples
│       │   ├── Gender
│       │   │   ├── GenderExample.ipynb
│       │   │   └── genderData.txt
│       │   ├── Iris
│       │   │   └── IrisExample.ipynb
│       │   └── NetworkTextAnalysis
│       │       ├── NetworkTextAnalysis.ipynb
│       │       └── text.txt
│       └── README.md
├── README.md
├── RegressionAnalysis
│   ├── CrossValidation
│   │   ├── CrossValidation.py
│   │   └── README.md
│   ├── DimensionReduction
│   │   ├── PrincipleComponentAnalysis
│   │   │   └── PCA.py
│   │   ├── PrincipleComponentRegression
│   │   │   └── PCR.py
│   │   └── README.md
│   ├── PartialLeastSquaresRegression
│   │   ├── PLSR.py
│   │   └── README.md
│   ├── README.md
│   └── UnaryLinearRegression
│       ├── ULR.py
│       └── data.txt
└── SolveEquations
    ├── Algorithms
    │   ├── NumericGeneticAlgorithm.py
    │   └── OneVarHighOrder.py
    ├── Examples
    │   └── Braking Distance Speed
    │       ├── BrakingDistance_Speed.py
    │       └── data.txt
    └── README.md

32 directories, 56 files
```

