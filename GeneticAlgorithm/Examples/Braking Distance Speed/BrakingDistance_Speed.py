# -*- coding: utf-8 -*-

'''
@program: BrakingDistance_Speed.py

@description: 刹车距离与车速的关系

@author: doubleZ

@create: 2020/02/08 
'''

import numpy as np
from GeneticAlgorithm.NumericGeneticAlgorithm import NGA

data = np.loadtxt('data.txt')
v, d = data[:,0], data[:,1]
v2, v3, v4 = v**2, v**3, v**4

# 使用数学理论方法直接求的k的最小值
def mathematic():
    k = np.sum(d*v2 - 0.75*v3)/np.sum(v4)
    return k

# 遗传算法所用的函数
def f(k):
    return np.abs(np.sum(d*v2 - 0.75*v3-k*v4))


if __name__ == '__main__':

    k = mathematic()
    print('数学理论推导结果 ', k)

    k = NGA(f, 0, max_times=100)
    print('遗传算法结果', k)