# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 14:20
@File: compose.py
@Tool: PyCharm 
"""

from vectors import scale, add
from teapot import load_triangles
from draw_model import draw_model


# currying
def compose(f1, f2):
    def new_function(input):
        return f1(f2(input))
    return new_function()


def scale_by(scalar):
    def new_func(v):
        return scale(scalar, v)
    return new_func


def translate_by(tv):
    def new_func(v):
        return add(tv, v)
    return new_func


def polygon_map(transformation, polygons: list):
    return [[transformation(vertex) for vertex in triangle] for triangle in polygons]


orit = load_triangles()
tf_polygon = polygon_map(scale_by(2), orit)
draw_model(tf_polygon)