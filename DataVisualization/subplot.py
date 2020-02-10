# -*- coding: utf-8 -*-

'''
@program: subplot.py

@description: 子图

@author: doubleZ

@create: 2020/02/10 
'''
import matplotlib.pyplot as plt
import numpy as np

def drawSubplots():
    x = np.linspace(0,5,10)

    fig, axes = plt.subplots(figsize=(8,6),dpi=100)
    axes.plot(x, x**2, 'r')
    axes.set_title('y=x^2')

    plt.show()

if __name__ == '__main__':
    drawSubplots()