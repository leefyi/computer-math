#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 16:42
# @Author  : lifangyi
# @File    : practice26.py
# @Software: PyCharm


# u=(1,-1)
# v=(n, m) 且n > m > 0， 它与u的距离为13
# 从u到v的位移是多少？ v与u做向量减法

from practice24 import subtract
from practice25 import distance


u = (1,-1)


rs = []
for n in range(-100,100):
    for m in range(-100, 100):
        v = (n,m)
        d = distance(v, u)
        if d==13 and n>m>0:
            rs.append((n,m))

print(rs)
# 如果有结果，那么从u到v的位移是啥？ 向量减法
sw = []
for r in rs:
    x=r[0]-u[0]
    y=r[1]-u[1]
    # subtract(r, u)
    sw.append((x,y))

print(sw)


