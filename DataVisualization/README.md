# Matplotlib制图数据可视化

Table of Contents
=================

   * [Matplotlib制图数据可视化](#matplotlib制图数据可视化)
      * [采样](#采样)
      * [颜色列表](#颜色列表)
      * [基础画图](#基础画图)
      * [常见图表](#常见图表)
         * [饼图](#饼图)
         * [散点图](#散点图)
         * [柱图](#柱图)
         * [柱图 折线图](#柱图折线图)
      * [子窗口](#子窗口)
      * [三维图](#三维图)
         * [trisurf](#trisurf)
         * [surface](#surface)
            * [等高线](#等高线)

------

- **解决中文乱码**

  ```python
  import matplotlib as mpl
  mpl.rcParams['axes.unicode_minus'] = False      # 解决汉字乱码
  mpl.rcParams['font.family'] = 'sans-serif'      # 负号正常显示
  mpl.rcParams['font.sans-serif'] = [u'SimHei']
  ```

## 采样

- `np.arange(start, end, step)`：起点、终点、采样间隔
  - 不包含终点
- `np.linspace(start, end, num, endpoint=True)`：开始值、终值、元素个数
  - 第四个参数指定是否包括终值

## 颜色列表

![image.png](https://upload-images.jianshu.io/upload_images/12014150-c28639a671f3482a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 基础画图

```python
x = np.arange(-np.pi, np.pi, .1)
y = np.sin(x)

plt.plot(x, y, color='r', linewidth=2.0, linestyle='--'， label='sin')
plt.grid(True)		# 网格线
plt.xlim(-5, 5)		# 横轴坐标范围
plt.ylim(-2, 2)		# 纵轴坐标范围
plt.xlabel('x')		# x轴标识
plt.ylabel('y=sin(x)')		# y轴标识
plt.title('figure of sin')	# 图像标题
xticks(np.linspace(-np.pi, np.pi, 5))		# 指定坐标轴刻度
legend(loc='upper left')		# 指定图例位置

plt.show()
```

## 常见图表

### 饼图

```python
plt.pie(data, explod=[0,0,0.2,0.0])		# explod的第三个参数意味着对应饼块被抛出饼
```

<img src="https://upload-images.jianshu.io/upload_images/12014150-2b56b3e1ea2d2a51.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:33%;" />

### 散点图

```python
plt.scatter(x,y,marker='v')
```

<img src="https://upload-images.jianshu.io/upload_images/12014150-4cb157c8f33c3d38.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:33%;" />

| **缩写** | **颜色**     | **缩写** | **颜色**           |
| -------- | ------------ | -------- | ------------------ |
| **“.”**  | 点标记       | “4”      | 右三角架标记       |
| **“,”**  | 像素标记     | “s”      | 正方形标记         |
| **“o”**  | 圆圈标记     | “p”      | 五角形标记         |
| **“v”**  | 倒三角标记   | “*”      | 星型标记           |
| **“^”**  | 正三角标记   | “H”      | 旋转六边形钻石标记 |
| **“<”**  | 左三角标记   | “d”      | 钻石标记           |
| **“>”**  | 右三角标记   | “\|”     | 竖线标记           |
| **“1”**  | 倒三角架标记 | “_”      | 水平线标记         |
| **“2”**  | 正三角架标记 | “+”      | +号标记            |
| **“3”**  | 左三角架标记 | “x”      | 十字交叉标记       |

### 柱图

```python
plt.bar(x=(0,1,2),height=(1,0.5,0.8),width=0.3,align='center')
```

<img src="https://upload-images.jianshu.io/upload_images/12014150-1053e661eb05528b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:33%;" />



### 柱图+折线图

```python
plt.plot(x, data, color='r')
plt.bar(x, data, alpha=.5, color='b', width=0.2, align='center')
```

<img src="https://upload-images.jianshu.io/upload_images/12014150-3792dc0ea8516f74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" style="zoom:33%;" />

------

## 子窗口

```python
plt.subplot(row, col, index)


fig, axes = plt.subplots(figsize=(8,6), dpi=100)
axes.plot(x,y)
axes.set_xlabel('')
axes.set_title('')
```

- figsize：800\*600像素
- dpi：每英寸100个点

------

## 三维图

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
```

### trisurf

以小三角形构成曲面单元，xyz是等长的1D array

```python
x, y, z = np.random.randint(1,10,5), np.random.randint(1,10,5), np.random.randint(1,10,5)
ax.plot_trisurf(x,y,z)
```

### surface

使用np.meshgrid产生数据，数据都是二维矩阵

```python
x_surf, y_surf = np.arange(0,1,.01), np.arange(0,1,.01)
x, y = np.meshgrid(x_surf, y_surf)
z = x + y
ax.plot_surface(x,y,z,cmap=cm.hot)
```

#### 等高线

```python
CS = plt.contour(X,Y,Z,10)
plt.clabel(CS, inline=1,fontsize=10, colors='k')		# 负值用虚线显示
```

