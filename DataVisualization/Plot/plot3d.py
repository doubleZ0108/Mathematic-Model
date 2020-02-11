# -*- coding: utf-8 -*-

'''
@program: plot3d.py

@description: 3D绘图

@author: doubleZ

@create: 2020/02/10 
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

def drawTrisurf():
    fig = plt.figure()
    ax = Axes3D(fig)
    x, y, z = np.random.randint(1,10,5), np.random.randint(1,10,5), np.random.randint(1,10,5)
    ax.plot_trisurf(x,y,z)
    plt.show()

def drawTrisurf_hard():
    n_angles, n_radii = 36, 8
    radii, angles = np.linspace(0.125, 1.0, n_radii), np.linspace(0,2*np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[...,np.newaxis], n_radii, axis=1)

    x, y = np.append(0,(radii*np.cos(angles)).flatten()), np.append(0,(radii*np.sin(angles)).flatten())
    z = np.sin(-x*y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_trisurf(x,y,z,cmap=plt.cm.jet)
    plt.show()

def drawSurface():
    x_surf, y_surf = np.arange(0, 1, .01), np.arange(0, 1, .01)
    x, y = np.meshgrid(x_surf, y_surf)
    z = x + y
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x, y, z, cmap=cm.hot)
    plt.show()


def drawSurface_with_Contour():
    '''等高线'''
    n=200
    x = np.linspace(-10.0, 10.0, n)
    y = np.linspace(-10.0, 10.0, n)
    s1 = 2 * np.exp(-((x + 1) / (3)) ** 2)
    # 生成一条高斯曲线 ,高斯峰公式  s=A*exp(-((x-w)/sigma)**2)
    s2 = 2 * np.exp(-((y + 2) / (3)) ** 2)
    Z1 = np.outer(s1, s2)  # 向量外积，生成第一个高斯山包
    w1 = 2 * np.exp(-((x - 2) / 4) ** 2)
    w2 = 2 * np.exp(-((y - 1) / 4) ** 2)
    Z2 = np.outer(w1, w2)  # 生成第二个高斯山包
    X, Y = np.meshgrid(x, y)
    Z = 100 * (Z2 - Z1)

    CS = plt.contour(X,Y,Z,10)
    plt.clabel(CS, inline=1,fontsize=10)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X,Y,Z,cmap=cm.jet)
    plt.show()



if __name__ == '__main__':
    drawSurface_with_Contour()