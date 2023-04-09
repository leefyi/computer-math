# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 14:05
@File: scale2.py
@Tool: PyCharm 
"""

from teapot import load_triangles
from vectors import scale
from draw_model import draw_model

# 将向量乘以标量2.0
def scale2(v):
    return scale(2.0, v)


original_triangles = load_triangles()
scaled_triangles = [
    [scale2(vertex) for vertex in triangle] for triangle in original_triangles
]

# 使用扩容后的三角形画大茶壶
draw_model(scaled_triangles)