# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/4/9 14:48
@File: practice2.py
@Tool: PyCharm
"""


from teapot import load_triangles
from draw_model import draw_model
from compose import translate_by


def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]



import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('ex_translate_teapot_down_z',[0])
####################################################################

origin_triangles = load_triangles()
new_triangles = polygon_map(translate_by((0,0,-20)), origin_triangles)
draw_model(new_triangles)
