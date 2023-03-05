#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 16:28
# @Author  : lifangyi
# @File    : practice19.py
# @Software: PyCharm

# 将定z=(-1,1)和v=(1,1)，而实数r和s，-3<r<3, -1<s<1。在平面上
# r*z+s*v 的终点可能在哪里？


import random

from vector_drawing import draw, Points
from practice17 import scale
from practice7 import add

z=(-1,1)
v=(1,1)
def random_r():
    return random.uniform(-3,3)

def random_s():
    return random.uniform(-1,1)


ps = []
for i in range(500):
    r1 = random_r()
    s1 = random_s()
    nz = scale(r1, z)
    nv  =scale(s1, v)
    ps.append(add(nz, nv))

draw(Points(*ps))