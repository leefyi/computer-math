# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 15:00
@File: upgrade_compose.py
@Tool: PyCharm 
"""

from math import pi

from rotate import rotate_z_by, rotate_x_by
from teapot import load_triangles
from draw_model import draw_model

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]


def compose(*args):
    def new_func(input):
        state = input
        for f in reversed(args):
            state = f(state)
            print(state)
        return state
    return new_func


def prepend(s):
    def new_func(input):
        return s+input
    return new_func


f = compose(prepend("P"), prepend("y"), prepend("t"))
r = f("hon")
print(r)

draw_model(polygon_map(compose(rotate_z_by(pi/2), rotate_x_by(pi/2)), load_triangles()))

