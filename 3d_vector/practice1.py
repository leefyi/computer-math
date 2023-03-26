# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/3/26 13:15
@File: practice1.py
@Tool: PyCharm 
"""


from draw3d import draw3d, Points3D, Arrow3D, Box3D

points = [(-1,-2,2)]

draw3d(

    Points3D(*points),
    Box3D(*points[0])
)