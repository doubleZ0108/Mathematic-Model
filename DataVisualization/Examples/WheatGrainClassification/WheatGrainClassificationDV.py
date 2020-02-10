# -*- coding: utf-8 -*-

'''
@program: WheatGrainClassificationDS.py

@description: 

@author: doubleZ

@create: 2020/02/10 
'''
from RegressionAnalysis.DimensionReduction.PrincipleComponentAnalysis import PCA
import numpy as np
import matplotlib.pyplot as plt


def WheatGrainClassificationDV():
    A = np.loadtxt("wheat_train_PCA_X.txt")
    B = np.loadtxt("wheat_train_PCA_Y.txt")
    aver = A.mean(axis=0)
    std = A.std(axis=0)
    A = (A - aver) / std

    pca = PCA.PCA(A)
    print(pca.SVDdecompose())
    T, P = pca.PCAdecompose(6)
    print(T.shape)
    cls1, cls2 = B == 1.0, B != 1.0
    plt.plot(T[cls1, 0], T[cls1, 1], 'ro')
    plt.plot(T[cls2, 0], T[cls2, 1], 'b^')
    plt.show()

if __name__ == '__main__':
    WheatGrainClassificationDV()