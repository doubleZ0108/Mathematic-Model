# -*- coding: utf-8 -*-

'''
@program: Genetic.py

@description: 遗传算法寻优

@author: doubleZ

@create: 2020/02/08 
'''

import random

'''
例. y = (x-2.5)^2
'''
def f1(x):
    return (x-2.5)**2

'''
例. y = x^3 -2x^2 + 1
'''
def f2(x):
    return x**3 - 2*x**2 + 1

def Genetic(fx, *args):     # 函数作为函数的参数；动态参数
    x0 = args[0]
    y0 = fx(x0)

    times = 0
    while times < 100:
        sign = random.randint(1, 10)
        delta = random.random()/10.0    # 避免跳跃
        x1 = x0+delta if sign%2==0 else x0-delta
        y1 = fx(x1)
        if y1 < y0:
            x0, y0 = x1, y1
        print('第',times,'次迭代, x = ', x0, ' y = ', y0)
        times += 1


if __name__ == '__main__':
    x0 = 5
    Genetic(f1, x0)
    Genetic(f2, x0)