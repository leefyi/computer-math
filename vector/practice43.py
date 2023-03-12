#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/12 14:27
# @Author  : lifangyi
# @File    : practice43.py
# @Software: PyCharm


# 实现一个regular_polygon(n)函数，返回一个规则的N变形的笛卡尔坐标集合(大小随意)

from math import pi
from python_triangle import to_cartesian

def regular_polygon(n: int):
    d = 1
    vcs = []
    for k in range(n):
        arc = 2*pi*(k/n)
        x,y = to_cartesian((1, arc))
        vcs.append((x,y))
    return vcs


if __name__ == '__main__':
    r = regular_polygon(7)
    print(r)