# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/3/26 13:30
@File: practice2.py
@Tool: PyCharm 
"""

from draw3d import Segment3D, Points3D, draw3d
pm1 = [1,-1]

vertices = [(x,y,z) for x in pm1 for y in pm1 for z in pm1]

edges = [((x,y,1),(x,y,-1)) for x in pm1 for y in pm1] + [((x,1, z),(x,-1,z)) for x in pm1 for z in pm1] + [((1,y, z),(-1,y,z)) for y in pm1 for z in pm1]

print(*edges[0])

draw3d(
    Points3D(*vertices),
    *[Segment3D(*edge) for edge in edges]
)