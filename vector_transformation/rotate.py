# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 14:31
@File: rotate.py
@Tool: PyCharm 
"""

from vectors import to_polar, to_cartesian
from teapot import load_triangles
from draw_model import draw_model
from math import pi


def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def rotate2d(angle, vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a+angle))


def rotate_z(angle, vector):
    x, y, z = vector
    new_x, new_y = rotate2d(angle, (x, y))
    return new_x, new_y, z


def rotate_z_by(angle):
    def new_func(vector):
        return rotate_z(angle, vector)
    return new_func


def rotate_x(angle, vector):
    x, y, z = vector
    new_y, new_z = rotate2d(angle, (y,z))
    return x, new_y, new_z


def rotate_x_by(angle):
    def new_func(vector):
        return rotate_x(angle, vector)
    return new_func


def rotate_y(angle, vector):
    x, y, z= vector
    new_x, new_z = rotate2d(angle, (x, z))
    return new_x, y, new_z


def rotate_y_by(angle):
    def new_func(vector):
        return rotate_y(angle, vector)
    return new_func


origin_triangles = load_triangles()
tf_triangles = polygon_map(rotate_x_by(pi/2.0), origin_triangles)
# 跃然纸上，茶壶翻转了90度
draw_model(tf_triangles)