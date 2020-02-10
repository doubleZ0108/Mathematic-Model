# -*- coding: utf-8 -*-

'''
@program: example.py

@description: 

@author: doubleZ

@create: 2020/02/10 
'''

from sklearn import datasets
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def irisDV():
    '''鸢尾花数据可视化—三维'''
    iris = datasets.load_iris()
    data, target = iris.data, iris.target

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(data[target==0,0],data[target==0,1],data[target==0,3], 'ro')
    ax.plot(data[target == 1, 0], data[target == 1, 1], data[target == 1, 3], 'b^')
    ax.plot(data[target == 2, 0], data[target == 2, 1], data[target == 2, 3], 'gv')
    ax.set_xlim(min(data[:,0]),max(data[:,0]))
    ax.set_ylim(min(data[:, 1]), max(data[:, 1]))
    ax.set_zlim(min(data[:, 3]), max(data[:, 2]))

    plt.show()

if __name__ == '__main__':
    irisDV()