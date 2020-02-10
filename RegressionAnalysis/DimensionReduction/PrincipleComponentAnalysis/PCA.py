# -*- coding: utf-8 -*-

'''
@program: PCA.py

@description: 主成分分析

@author: doubleZ

@create: 2020/02/09 
'''

import numpy as np

class PCA:
    def __init__(self, X):
        self.X = X

    def SVDdecompose(self):
        B = np.linalg.svd(self.X, full_matrices=False)
        self.lamda = lamda = B[1]
        self.P = B[2].T
        self.T = B[0]*B[1]
        compare = [lamda[i]/lamda[i+1] for i in range(len(lamda)-1)]
        return np.array(compare)

    def PCAdecompose(self, k):
        """
        :param k: 主成分数
        :return: 去除噪声后的得分T和载荷P
        """
        T = self.T[:,:k]
        P = self.P[:,:k]
        return T,P

if __name__ == '__main__':
    '''根据数据，生成pca对象'''
    S = np.loadtxt('')
    pca = PCA(S)
    '''调用SVDdecompose获取特征比值，确定主成分'''
    compare = pca.SVDdecompose()
    print(compare)
    '''调用PCAdecompose，设定得分和载荷矩阵'''
    k = int(input('确定主成分数: '))
    T,P = pca.PCAdecompose(k)