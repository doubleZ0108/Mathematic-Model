# -*- coding: utf-8 -*-

'''
@program: PCR.py

@description: 主成分回归

@author: doubleZ

@create: 2020/02/09 
'''

import numpy as np
from RegressionAnalysis.DimensionReduction.PrincipleComponentAnalysis import PCA

class PCR:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def confimPCs(self):
        self.pca = PCA(self.X)
        compare = self.pca.SVDdecompose()
        return compare

    def model(self, PCs):
        T,P = self.pca.PCAdecompose(PCs)
        self.P = P
        oneCol = np.ones(T.shape[0])
        T = np.c_[oneCol, T]
        self.mlr = MLR(T,self.Y)
        self.mlr.model()
        self.A = self.mlr.getCoef()

    def predict(self, Xnew):
        T = np.dot(Xnew, self.P)
        oneCol = np.ones(T.shape[0])
        T = np.c_[oneCol, T]
        return self.mlr.predict(T)

    def fTest(self, arfa):
        return self.mlr.fTest(arfa)

if __name__ == '__main__':
    data = np.loadtxt('')
    X, Y = data[:-1].T, data[-1]
    trainX, trainY = X[:-3], Y[:-3]
    testX,testY = X[-3:],Y[-3:]

    pcr = PCR(trainX, trainY)
    compare = pcr.confimPCs()
    print(compare)

    k = int(input('确定主成分数: '))
    pcr.model(k)
    yHat = pcr.predict(testX)
    err = (testY-yHat)/testY*100
    print(err)
