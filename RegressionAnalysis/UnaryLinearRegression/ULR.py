# -*- coding: utf-8 -*-

'''
@program: ULR.py

@description: 一元线性回归

@author: doubleZ

@create: 2020/02/09 
'''
import math

import numpy as np
from scipy.stats import f, t

class ULR:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def model(self):
        Xt = self.X.T
        XtX = np.dot(Xt, self.X)
        XtXinv = np.linalg.inv(XtX)
        temp = np.dot(XtXinv, Xt)
        self.A = np.dot(temp, self.Y)

    def getCoef(self):
        """
        回归系数
        """
        return self.A

    def predict(self, X):
        """
        回归预测
        """
        return np.dot(X, self.A)

    def fTest(self, alpha):
        """
        f检验
        :param alpha: 置信度
        :return: F f临界 F>临界
        """
        n = len(self.X)     # 获取样本数
        f_arfa = f.isf(alpha, 1, n-2)   # f临界值
        Yaver = self.Y.mean()       # y平均值
        Yhat = self.predict(self.X) # 预测y
        U = ((Yhat-Yaver)**2).sum() # U值
        Qe = ((self.Y-Yhat)**2).sum()   # Qe值
        F = U/(Qe/(n-2))        # f值
        answer = [F, f_arfa, F>f_arfa]
        return answer

    def rTest(self, alpha):
        """
        r检验
        :param alpha: 置信度
        :return: r r临界 r>临界
        """
        n = len(self.X)
        f_arfa = f.isf(alpha, 1, n-2)
        r_arfa = math.sqrt(1.0/(1+(n-2)/f_arfa))
        X = self.X[:,1]
        Xaver, Yaver = X.mean(), self.Y.mean()
        fenzi1, fenzi2 = X - Xaver, self.Y - Yaver
        fenzi = (fenzi1*fenzi2).sum()
        fenmu1 = ((X-Xaver)**2).sum()
        fenmu2 = ((self.Y-Yaver)**2).sum()
        fenmu = math.sqrt(fenmu1*fenmu2)
        r = math.fabs(fenzi/fenmu)
        return [r, r_arfa, r>r_arfa]


if __name__ == '__main__':
    '''整理数据'''
    data = np.loadtxt('data.txt').T
    Y, X = data[:,0], data[:,1]
    oneCol = np.ones(X.shape[0])
    X = np.c_[oneCol, X]        # 将原来的X加一列，一球截距

    '''调用ULR类'''
    ulr = ULR(X, Y)
    ulr.model()
    print(ulr.getCoef())

    '''回归预测'''
    Xnew = np.array([1, 1.68])
    leg = ulr.predict(Xnew)
    print(leg)

    '''t检验'''
    fTest = ulr.fTest(0.05)
    print(fTest)

    '''r检验'''
    rTest = ulr.rTest(0.05)
    print(rTest)