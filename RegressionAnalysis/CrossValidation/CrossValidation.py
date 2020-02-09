# -*- coding: utf-8 -*-

'''
@program: CrossValidation.py

@description: 交叉验证

@author: doubleZ

@create: 2020/02/09 
'''

import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import KFold

def cvPVS():
    yTrue, yHat = None, None

    '''经典的交叉验证'''
    pls = PLSRegression(n_components=4, scale=False)  # 4主成分
    for train_index, test_index in kf.split(X):  # 建模、测试样本编号
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]
        pls.fit(X_train, Y_train)
        c_pred = pls.predict(X_test)[:, 0]

        if yTrue is None:  # 第一份预测
            yTrue = Y_test  # 真值
            yHat = c_pred  # 预测值
        else:
            yTrue = np.r_[yTrue, Y_test]  # 后续预测，进行行叠加
            yHat = np.r_[yHat, c_pred]

    '''计算每个样本的预测误差'''
    print(np.abs(yTrue - yHat) / yTrue * 100)
    print(np.sum(np.abs(yTrue - yHat) / yTrue * 100) / len(X))  # 平均%误差

if __name__ == '__main__':
    data = np.loadtxt('')
    X, Y = data[:-1].T, data[-1]

    kf = KFold(n_splits=10)     # 十分交叉验证

    cvPVS()
