#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 16:37
# @Author  : lifangyi
# @File    : practice25.py
# @Software: PyCharm


# 实现distance(v1,v2)
# 返回两个向量之间的距离

from vectors import length
from practice3 import dino_vectors
from practice24 import subtract


def distance(v1, v2):
    return length(subtract(v1,v2))


# 计算恐龙周长
def perimeter(vector_list):
    l = 0.0
    for i in range(len(vector_list)):
        v1 = vector_list[i]
        v2 = vector_list[(i+1)%len(vector_list)]
        sl = distance(v1, v2)
        l += sl

    return l


pl = perimeter(dino_vectors)
print(pl)