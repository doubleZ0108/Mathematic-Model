# -*- coding: utf-8 -*-

'''
@program: PLSR.py

@description: 

@author: doubleZ

@create: 2020/02/09 
'''

from sklearn.cross_decomposition import PLSRegression

'''建模'''
pls = PLSRegression(n_components=k, scale=True)

'''预报'''
Ypred = pls.predict(Xnew)