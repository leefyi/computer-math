# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 14:11
@File: shift_1.py
@Tool: PyCharm 
"""

from vectors import add
from teapot import load_triangles
from draw_model import draw_model

def translate1left(v):
    return add((-1,0,0), v)


original_triangles = load_triangles()
scaled_translated_triangles = [
    [translate1left(vertex) for vertex in triangle] for triangle in original_triangles
]

draw_model((scaled_translated_triangles))