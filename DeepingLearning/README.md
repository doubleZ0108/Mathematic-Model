# KERAS深度学习

[TOC]

------

## 模型搭建

- 通过Sequential对象堆叠而成
- 用Sequential的add方法增加网络层，确定网络每层的拓扑及激活函数
- 新网络层的生成，使用 Dense对象完成，设置节点、激活函数
- 用compile方法编译模型
- fit方法训练模型
- predict方法预测新数据

1. 引用

   ```python
   from keras.models import Sequential
   from keras.layers import Dense
   ```

2. 生成模型

   ```python
   model = Sequential()
   ```

3. 增加网络层

   ```python
   # 输入层
   model.add(Dense(units=5, activation='relu',input_dim=2))  #  需要input_dim参数
   # 输出层
   model.add(Dense(units=2, activation= 'softmax'))
   ```

4. 编译模型

   ```python
   model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
   ```

5. 训练和预报

   ```python
   model.fit(Xtrain, ytrain, epochs=100, batch_size=5)
   classes = model.predict(Xtest, batch_size=5)
   ```