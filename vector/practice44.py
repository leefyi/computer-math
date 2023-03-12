#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/12 14:27
# @Author  : lifangyi
# @File    : practice44.py
# @Software: PyCharm

# 将恐龙先按向量(8,8)平移，再将其旋转5pi/3(以原点为圆心)

from math import pi

from practice3 import dino_vectors
from vectors import translate
from rotate import rotate
from vector_drawing import draw, Polygon, Points


# 平移
# 旋转（笛卡尔坐标转换为极坐标，旋转，再转换为笛卡尔坐标）
# 画图
print(dino_vectors)

tld_dino = translate((8, 8), dino_vectors)
print(tld_dino)
# draw(Polygon(*tld_dino))
rtd_dino = rotate(tld_dino, 5*pi/3)

print(rtd_dino)
draw(Points(*rtd_dino), Polygon(*rtd_dino))