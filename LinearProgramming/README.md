# 最优化建模 | 线性规划

[TOC]

------

在约束条件下，求解线性目标函数的极值问题

## Scipy.optimize.minimize

最小化，对最大值问题可取附属

1. 定义优化函数

   ```python
   def func(x):
     return -(0.5*sqrt(x[0]*15+x[1]*5)+0.5*sqrt(x[0]*5+x[1]*12))
   ```

2. 将每个限制条件定义为一个函数，以$f(x)>=0$形式

   ```python
   fun1 = lambda x: 10-x[0]-x[1]
   ```

3. 确定搜索边界(用字典形式表示)

   ```python
   _constraints = ({'type':'ineq','fun':fun1})     # ineq->不等于
   _bounds = ((0,10),(0,10))   # 优化范围
   ```

4. 求解

   ```python
   result = so.minimize(func, (5,5), method='SLSQP', bounds=_bounds, constraints=_constraints)
   ```

### 优化算法

-  BFGS
- Nelder-Mead单纯形
- 牛顿共轭梯度
- COBYLA或SLSQP