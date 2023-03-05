#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 14:01
# @Author  : lifangyi
# @File    : practice2.py
# @Software: PyCharm

# 画一条（0,0）到(2,-2)的箭头


from vector_drawing import Points, Arrow, draw


vectors = [(0,0),(2,-2)]
p = Points(*vectors)
ar = Arrow(tip=vectors[1],tail=vectors[0])
draw(p,ar)