# -*- coding: utf-8 -*-

'''
@program: buf.py

@description: 

@author: doubleZ

@create: 2020/02/08 
'''

def func(li):
    for i in range(len(li)):
        li[i] *= 10

li = [1, 2, 3]
func(li)
print(li)