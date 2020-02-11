# -*- coding: utf-8 -*-

'''
@program: example.py

@description: 线性规划例子

@author: doubleZ

@create: 2020/02/11 
'''
from math import sqrt
import scipy.optimize as so

'''
【单约束】
f(x) = ...
100 >= a*10 + b*10
a,b>=0
'''
def solveOneConstraints():
    '''定义优化函数'''
    def func(x):
        return -(0.5*sqrt(x[0]*15+x[1]*5)+0.5*sqrt(x[0]*5+x[1]*12))

    '''将每个限制条件定义为函数形式（>=0形式）'''
    fun1 = lambda x: 10-x[0]-x[1]

    '''确定搜索边界，用字典定义'''
    _constraints = ({'type':'ineq','fun':fun1})     # ineq->不等于
    _bounds = ((0,10),(0,10))   # 优化范围

    result = so.minimize(func, (5,5), method='SLSQP', bounds=_bounds, constraints=_constraints)
    print(result)

'''
【多约束】
Min((x1-1)^2+(x2-2.5)^2) 
x1-2x2+2>=0 
-x1-2x2+6>=0 
-x1+2x2+2>=0 
x1,x2>=0
'''
def solveMultiConstraints():
    fun = lambda x: (x[0]-1)**2 + (x[1]-2.5)**2

    fun1 = lambda x: x[0]-2*x[1]+2
    fun2 = lambda x: -x[0]-2*x[1]+6
    fun3 = lambda x: -x[0]+2*x[1]+2
    _constraints = (
        {'type': 'ineq', 'fun': fun1},
        {'type': 'ineq', 'fun': fun2},
        {'type': 'ineq', 'fun': fun3}
    )
    _bounds = ((0,None),(0,None))

    result = so.minimize(fun, (2,0), method='SLSQP', bounds=_bounds, constraints=_constraints)
    print(result)


if __name__ == '__main__':
    solveMultiConstraints()
