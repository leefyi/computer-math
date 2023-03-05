#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 15:24
# @Author  : lifangyi
# @File    : practice11.py
# @Software: PyCharm

# 绘制100个互不重叠的恐龙

# 估算恐龙的大致尺寸，最高12，最宽9
# 我们做100种平移，得到100组向量集合
# 然后对100组向量集合作图

from vector_drawing import Polygon, draw

from practice8 import translate


dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

# 10*10
translations = [(12*x,9*y) for x in range(-5,5) for y in range(-5,5)]

rv = []
for t in translations:
    rv.append(translate(t, dino_vectors))

dinos = []
# 每一组新向量
for v in rv:
    dino = Polygon(*v, color=blue)
    dinos.append(dino)

draw(*dinos, grid=None)





