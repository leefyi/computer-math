#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 15:16
# @Author  : lifangyi
# @File    : practice5.py
# @Software: PyCharm

from vector_drawing import Points, draw


vectors = [(x, x**2) for x in range(-10,11)]

p = Points(*vectors)

draw(
    p,
    grid=(1,10),
    nice_aspect_ratio=False
)