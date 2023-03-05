#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 14:22
# @Author  : lifangyi
# @File    : practice4.py
# @Software: PyCharm


from practice3 import dino_vectors

from vector_drawing import draw, Points, Polygon


draw(Points(*dino_vectors),
     Polygon(*dino_vectors))