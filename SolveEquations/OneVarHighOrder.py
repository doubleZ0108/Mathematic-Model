# -*- coding: utf-8 -*-

'''
@program: OneVarHighOrder.py

@description: 一元高次方程

@author: doubleZ

@create: 2020/02/08 
'''


'''
y = x^3 = 10^(-4.56) * x^2 - (10^(-4.56) * 0.01 + 10(-14) * x - 10^(-4.56) * 10^(-14_
'''
def f(x):
    ka = pow(10, -4.56)
    return x**3 + ka * x**2 - (0.01*ka + 1e-4) * x - ka*1e-4

def solveOneVarHighOrderEq(a, b):
    """
    计算一元高次方程在a，b点之间点根
    :param a: 区间左端点
    :param b: 区间右端点
    :return None: (a,b)间无实数根
    :return m: 精度为1e-8的实数根
    """
    if f(a) * f(b) > 0:
        print('根不在a, b之间')
        return None

    while abs(a - b) > 1e-8:
        m = (a + b) / 2
        if f(m) * f(a) > 0:
            a = m
        else:
            b = m
    return m


if __name__ == '__main__':
    _inf, inf = -100, 100
    result = solveOneVarHighOrderEq(_inf, inf)
    print(result)