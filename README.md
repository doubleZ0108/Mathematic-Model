# 数学模型 | Mathematic Model

Table of Contents
=================

   * [数学模型 | Mathematic Model](#数学模型--mathematic-model)
      * [关于作者 | About the Auther](#关于作者--about-the-auther)
      * [开发环境 | Development Environment](#开发环境--development-environment)
      * [基础数学模型 | Basic Mathematical Model](#基础数学模型--basic-mathematical-model)
      * [项目结构 | Project Structure](#项目结构--project-structure)

------

## 关于作者 | About the Auther

| 姓名 \| Name:bust_in_silhouette: | 张喆 \| doubleZ          |
| ----------------------------------------- | ------------------------ |
| 学校 \| University:school:             | 同济大学 \| Tongji Univ. |
| 联系方式 \| Email:email:                  | doubleZ0108@163.com      |

​	

## 开发环境 | Development Environment

- **操作系统 | Operating System**: macOS Catalina 10.15.2
- **IDE**: 
  - Jupiter notebook 6.0.1
  - PyCharm 2019.3.2
- **语言 | Language**: python
- **主要依赖 | Dependances**: sklearn, keras, scipy, numpy, matploblib, Axes3D, PIL

​	

## 基础数学模型 | Basic Mathematical Model

- **方程 | Euqation**

  - [夹逼法求解一元高次方程 | Squeeze Theorem](https://github.com/doubleZ0108/Mathematic-Model/tree/master/SolveEquations/SqueezeTheorem)

- **矩阵 | Matrix**

  - [基础运算 | Basic Operation](https://github.com/doubleZ0108/Mathematic-Model/tree/master/Matrix)
  - [奇艺值分解 | SVD](https://github.com/doubleZ0108/Mathematic-Model/tree/master/Matrix)

- **遗传算法 | Genetic Algorithm**

  - [数值遗传算法寻优 | NGA for Optimization](https://github.com/doubleZ0108/Mathematic-Model/tree/master/GeneticAlgorithm)

    > 🌰[刹车距离与车速关系 | The relationship between braking distance and speed](https://github.com/doubleZ0108/Mathematic-Model/tree/master/GeneticAlgorithm/Examples/Braking%20Distance%20Speed)

  - [数值遗传算法 | NGA](https://github.com/doubleZ0108/Mathematic-Model/tree/master/GeneticAlgorithm)

- **回归分析 Regression Analysis**

  - [线性回归 | Linear Regression](https://github.com/doubleZ0108/Mathematic-Model/tree/master/RegressionAnalysis)
    - [一元线性回归 | Unitary Linear Regression](https://github.com/doubleZ0108/Mathematic-Model/tree/master/RegressionAnalysis/UnaryLinearRegression)
    - [多元线性回归 | Multiple Linear Regression](https://github.com/doubleZ0108/Mathematic-Model/tree/master/RegressionAnalysis)
  - [降维回归 | Dimension Reduction](https://github.com/doubleZ0108/Mathematic-Model/tree/master/RegressionAnalysis/DimensionReduction)
    - 主成分分析 | PCA
    - 主成分回归 | PCR
  - [偏最小二乘法 | PLSR](https://github.com/doubleZ0108/Mathematic-Model/tree/master/RegressionAnalysis/PartialLeastSquaresRegression)
  - [交叉验证 | Cross Validation](https://github.com/doubleZ0108/Mathematic-Model/tree/master/RegressionAnalysis/CrossValidation)

- **数据可视化 | Data Visualization**

  - [常见图表 | Basic Chart](https://github.com/doubleZ0108/Mathematic-Model/blob/master/DataVisualization/Plot/plot.py)

  - [三维图像 | 3D Fingure](https://github.com/doubleZ0108/Mathematic-Model/blob/master/DataVisualization/Plot/plot3d.py)

  - [聚类分析 | Clustering Analysis](https://github.com/doubleZ0108/Mathematic-Model/tree/master/DataVisualization/Examples)

    - 无监督 | Unsupervised
    - 有监督 | PLSDA
    - 概率等高线模拟 | Probability Contour Simulation

    > 🌰[鸢尾花数据可视化 | Iris data visualization](https://github.com/doubleZ0108/Mathematic-Model/tree/master/DataVisualization/Examples/Iris)
    >
    > 🌰[小麦优、劣颗粒分类聚类可视化 | Visualization of classification and clustering of superior and inferior grains in wheat](https://github.com/doubleZ0108/Mathematic-Model/tree/master/DataVisualization/Examples/WheatGrainClassification)

- **神经网络 | Neural Network**

  - [神经网络 | Neural Network](https://github.com/doubleZ0108/Mathematic-Model/tree/master/NeuralNetwork)

  - [非线性分类 | Nonlinear Classification](https://github.com/doubleZ0108/Mathematic-Model/tree/master/NeuralNetwork)

  - [MLPClassifier神经网络 | MLPC](https://github.com/doubleZ0108/Mathematic-Model/tree/master/NeuralNetwork)

  - [MLPRegressor神经网络回归 | MLPR](https://github.com/doubleZ0108/Mathematic-Model/tree/master/NeuralNetwork)

    > 🌰[手写数字图像识别 | Handwritten Digit Recognition](https://github.com/doubleZ0108/Mathematic-Model/tree/master/NeuralNetwork/HandwrittenDigitRecognition)

- **最优化建模 | Optimization**

  - [线性规划 | Linear Programming](https://github.com/doubleZ0108/Mathematic-Model/tree/master/Optimization/LinearProgramming)

- **深度学习 | Deep Learning**

  - [Keras深度学习模型 | Keras](https://github.com/doubleZ0108/Mathematic-Model/tree/master/DeepLearning/Keras)

    > 🌰[手写数字图像识别 | Handwritten Digit Recognition](https://github.com/doubleZ0108/Mathematic-Model/blob/master/DeepLearning/Keras/Examples/HandwrittenDigitRecognition_DL.ipynb)
    >
    > 🌰[小麦分类 | Classification of wheat](https://github.com/doubleZ0108/Mathematic-Model/blob/master/DeepLearning/Keras/Examples/Wheat/wheat.ipynb)

- **概率建模 | Probability**

  - [朴素贝叶斯概率建模 | NBM](https://github.com/doubleZ0108/Mathematic-Model/tree/master/Probability/NaiveBayesianModel)

    > 🌰[身高体重等与性别的关系](https://github.com/doubleZ0108/Mathematic-Model/blob/master/Probability/NaiveBayesianModel/Examples/Gender/GenderExample.ipynb)
    >
    > 🌰[鸢尾花数据分类](https://github.com/doubleZ0108/Mathematic-Model/blob/master/Probability/NaiveBayesianModel/Examples/Iris/IrisExample.ipynb)
    >
    > 🌰[网络文本分析](https://github.com/doubleZ0108/Mathematic-Model/blob/master/Probability/NaiveBayesianModel/Examples/NetworkTextAnalysis/NetworkTextAnalysis.ipynb)

​	

## 项目结构 | Project Structure

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
├── DeepLearning
│   └── Keras
│       ├── Examples
│       │   ├── HandwrittenDigitRecongnition_DL.ipynb
│       │   └── Wheat
│       │       ├── wheat.ipynb
│       │       ├── wheat_train_PCA_X.txt
│       │       └── wheat_train_PCA_Y.txt
│       ├── Keras.ipynb
│       └── README.md
├── GeneticAlgorithm
│   ├── Examples
│   │   └── Braking Distance Speed
│   │       ├── BrakingDistance_Speed.py
│   │       └── data.txt
│   ├── Individual.py
│   ├── NumericGeneticAlgorithm.py
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
├── Optimization
│   └── LinearProgramming
│       ├── Examples
│       │   └── example.py
│       └── README.md
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
    └── SqueezeTheorem
        ├── OneVarHighOrder.py
        └── README.md

34 directories, 56 files
```

