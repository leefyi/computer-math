# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/3/26 14:03
@File: practice3.py
@Tool: PyCharm 
"""

from draw3d import Arrow3D, draw3d
from colors import red, blue, purple


draw3d(
    Arrow3D((4,0,3), color=red),
    Arrow3D((-1,0,1), color=blue),
    Arrow3D((3,0,4),(4,0,3), color=blue),
    Arrow3D((-1,0,1),(3,0,4), color=red),
    Arrow3D((3,0,4), color=purple)

)