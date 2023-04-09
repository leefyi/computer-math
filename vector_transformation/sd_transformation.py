# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 14:41
@File: sd_transformation.py
@Tool: PyCharm
"""

from teapot import load_triangles
from draw_model import draw_model


def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]


def stretch_x(vector):
    x, y, z = vector
    return (4 * x, y, z)


def cube_y(vector):
    x, y, z = vector
    return (x, y * y * y, z)


# 使茶壶倾斜
def slant_xy(vector):
    x, y, z = vector
    return (x + y, y, z)


origin_triangles = load_triangles()
# new_triangles = polygon_map(stretch_x, origin_triangles)
# draw_model(new_triangles)

# new_triangles = polygon_map(cube_y, origin_triangles)
# draw_model(new_triangles)

new_triangles = polygon_map(slant_xy, origin_triangles)
draw_model(new_triangles)
