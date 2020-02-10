# -*- coding: utf-8 -*-

'''
@program: plot.py

@description: 

@author: doubleZ

@create: 2020/02/09 
'''

from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False      # 解决汉字乱码
mpl.rcParams['font.family'] = 'sans-serif'      # 负号正常显示
mpl.rcParams['font.sans-serif'] = [u'SimHei']


def drawCurve():
    x = np.arange(-np.pi, np.pi, .1)
    y = np.sin(x)
    y1 = np.cos(x)

    plt.plot(x, y, color='r', linewidth=2.0, linestyle='--', label='sin')
    plt.plot(x, y1, color='b', label='cos')

    plt.grid(True)
    plt.xlim(-5, 5)
    plt.ylim(-2, 2)
    plt.xlabel('x')
    plt.ylabel('y=sin(x)')
    plt.title('figure of sin')
    xticks(np.linspace(-np.pi, np.pi, 5))
    legend()

    plt.show()

def drawPie():
    data = np.random.randint(1,11,5)
    plt.pie(data, explode=[0,0,0.2,0,0])
    plt.show()

def drawScatter():
    n = 100
    x, y = np.random.normal(0,1,n), np.random.normal(0,1,n)
    plt.scatter(x,y,marker='v')
    plt.show()

def drawBar():
    plt.bar(x=(0,1,2),height=(1,0.5,0.8),width=0.3,align='center')
    plt.show()

def drawBar_with_Curve():
    data = np.random.randint(1, 10, 5)
    x = np.arange(len(data))
    plt.plot(x, data, color='r')
    plt.bar(x, data, alpha=.5, color='b', width=0.2, align='center')
    plt.show()

if __name__ == '__main__':
    drawBar_with_Curve()