#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/12 14:21
# @Author  : lifangyi
# @File    : rotate.py
# @Software: PyCharm


# 实现向量的逆时针旋转函数
# 接受笛卡尔坐标集合和一个固定的弧度

from math import sin, cos, atan2, pow, sqrt, pi


def rotate(vectors, arc):
    nv = []
    for vector in vectors:
        x, y = vector[0], vector[1]
        l = sqrt(pow(x, 2) + pow(y, 2))
        ac = atan2(y, x)
        aca = (ac + arc) % (2*pi)
        ny = sin(aca)*l
        nx = cos(aca)*l
        nv.append((nx, ny))
    return nv

