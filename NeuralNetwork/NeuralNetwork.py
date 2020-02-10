# -*- coding: utf-8 -*-

'''
@program: NeuralNetwork.py

@description: 神经网络

@author: doubleZ

@create: 2020/02/10 
'''

import numpy as np

class NeuralNetwork:
    '''激活函数及其导数'''
    def logistic(self,x):
        return 1/(1+np.exp(-x))
    def logistic_deriv(self,x):
        return self.logistic(x)*(1-self.logistic(x))
    def tanh(self,x):
        return np.tanh(x)
    def tanh_deriv(self,x):
        return 1.0-np.tanh(x)**2

    def __init__(self, layers, activation='tanh'):
        """
        :param layers: 元组（输入、隐、输出节点数）
        :param activation:
        """
        self.activation = self.logistic if activation=='logistic' else self.tanh
        self.activation_deriv = self.logistic_deriv if activation=='logistic' else self.tanh_deriv
        self.weights = []   # 两层间的权重
        for i in range(len(layers)-1):      # -1~1间的随机数
            if i==0:
                w = 2*np.random.random((layers[0]+1, layers[1]))-1
                self.weights.append(w*0.5)
            else:
                w = 2*np.random.random((layers[i], layers[i+1]))-1
                self.weights.append(w*0.5)

    def fit(self,X,y,learning_rate=0.2,epochs=10000):
        """
        训练函数
        :param X: 每行是一个样本的特征
        :param y: 对应的分类
        :param learning_rate: 学习速率
        :param epochs: 进行学习的最大次数
        :return:
        """
        temp = np.ones(X.shape[0])
        X = np.c_[X, temp]      # bias 加一列
        for k in range(epochs):
            # 随机选取一个样本，对神经网络进行更新
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            # 完成所有正向的输出计算
            for j in range(len(self.weights)):
                a.append(self.activation(np.dot(a[j], self.weights[j])))
            error = y[i] - a[-1]    # 输出层在[-1]
            deltas = [error * self.activation_deriv(a[-1])]
            # 反向误差传播，更新权重
            for j in range(len(a)-2, 0, -1):    # 从倒第二层到开始层
                deltas.append(deltas[-1].dot(self.weights[j].T)*self.activation_deriv(a[j]))
            deltas.reverse()
            # 更新权重
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])    # 向量转成一行的矩阵
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        """
        预测
        :param x: 一组预测样本
        :return: 预测的结果
        """
        temp = np.ones(x.shape[0])
        x = np.c_[x, temp]  # 加偏置
        ans = []
        for a in x:
            for w in self.weights:
                a = self.activation(np.dot(a, w))
            ans.append(np.argmax(a))    # 输出层节点正交化
        return ans

