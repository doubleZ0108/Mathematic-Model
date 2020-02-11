# -*- coding: utf-8 -*-

'''
@program: HandwrittenDigitRecongnition.py

@description: 

@author: doubleZ

@create: 2020/02/11 
'''

import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

class ImageDigit:
    def __init__(self, img_name):
        self.im = Image.open(img_name).convert('L')  # 转换为灰度图像
        self.img_dirname = 'data/img/'
        self.img_32_32_dirname = 'data/img_32_32/'

    def histShow(self):
        """
        显示原图像直方图
        """
        im_arr = np.array(self.im)
        plt.figure("hist")
        arr = im_arr.flatten()
        n, bins, patches = plt.hist(arr, bins=256, density=1, facecolor='green', alpha=0.75)
        plt.show()

    def convert_to_bw(self, threshold):
        """
        将原图转换为黑白二值图像
        :param threshold: 阈值处理门限
        """
        self.im = self.im.point(lambda x: 255 if x > threshold else 0)  # 阈值处理
        self.im = self.im.convert('1')  # 黑白二值图像

    def split(self):
        """
        将小数字方块分割出来，存储到img_dirname文件夹下
        """
        assert self.im.mode == '1'
        w, h = self.im.size
        xs = [0, 31, 65, 91, 122, 150, 182, 211, 242, 271, w]
        ys = [0, 47, 93, 137, 185, 232, h]
        for i, x in enumerate(xs):
            if i + 1 >= len(xs):
                break
            for j, y in enumerate(ys):
                if j + 1 >= len(ys):
                    break
                box = (x, y, xs[i + 1], ys[j + 1])  # 一个字符所在图像的位置
                t = self.im.crop(box).copy()  # 将字符挖出来
                t.save(self.img_dirname + str((i + 1) % 10) + '_' + str(j) + '.bmp')

    def standardizing_to_32_32(self):
        """
        对所有图像进行标准化
        每个图像大小都是32*32， 且字符的上下、左右边距一样
        """
        for i in range(10):
            for j in range(6):
                im = Image.open(self.img_dirname + str(i) + '_' + str(j) + '.bmp')
                self.standardizing_to_32_32(im, i, j)

    def standardizing_to_32_32(self, im, ii, jj):
        """
        对一个小图像进行标准化
        :param im: 待标准化对小图像
        :param ii: 名字
        :param jj: 名字
        """
        w, h = self.im.size
        xrow, ycol = [], []
        for i in range(w):
            for j in range(h):
                pixel = self.im.getpixel((i, j))
                if (pixel < 1):
                    xrow.append(i)
                    ycol.append(j)
                    # 字符的长度、宽度
                    xLength, yLength = max(xrow) - min(xrow) + 1, max(ycol) - min(ycol) + 1
                    # 定义左、上、右、下的坐标
                    box = (min(xrow), min(ycol), max(xrow) + 1, max(ycol) + 1)
                    # 一个矩形区域的拷贝
                    t = self.im.crop(box).copy()
                    # 居中
                    xStart, yStart = (32 - xLength) // 2, (32 - yLength) // 2
                    bg = Image.new('RGB', (32, 32), 'white')
                    # 将一张图粘贴到另一张图像上
                    bg.paste(t, (xStart, yStart))
                    bg.save(self.img_32_32_dirname + str(ii) + '_' + str(jj) + "_32_32.bmp")

    def featureExtract(self):
        """
        特征提取
        将字符图像表达成256维向量
        :return: 输入数据X，输出点真值Y
        """
        netTrainDataInput = []  # 存储输入数据 X
        netTrainDataOutput = []  # 存储输出点真值 Y
        for i in range(10):
            outNode = [0.0] * 10
            outNode[i] = 1.0  # 训练集函数的真值，每种模式对应的位置数字为1
            for j in range(6):
                im = Image.open(self.img_32_32_dirname + str(i) + '_' + str(j) + '_32_32.bmp')
                f = self.featureExtract(im)
                netTrainDataInput.append(f)
                netTrainDataOutput.append(outNode)
        X = np.array(netTrainDataInput)
        y = np.array(netTrainDataOutput)
        return X, y

    def featureExtract(self, im):
        """
        计算一个小图像的特征向量
        :param im: 小图像
        :return: 特征向量
        """
        y = np.array([0,1])
        features = []
        for j in range(16):
            x = np.array([0,1])
            for i in range(16):
                box = (x[0],y[0],x[1]+1,y[1]+1)  # 2*2开区间
                t = self.im.crop(box).copy()
                count = 0.0
                for ii in range(2):
                    for jj in range(2):
                        pixel = t.getpixel((ii,jj))
                        if(pixel < 1):
                            count += 1.0
                features.append(count)
                x += 2  # 整个矩阵向右平移
            y += 2
        return features

if __name__ == '__main__':
    im = Image.open(r'handwritting.png')
    imgToDigit = ImageDigit(im)
    imgToDigit.histShow()
    threshold = int(input('请输入背景阈值: '))
    imgToDigit.convert_to_bw(threshold)
    imgToDigit.split()
    imgToDigit.standardizing_to_32_32()
    X, y = imgToDigit.featureExtract()
