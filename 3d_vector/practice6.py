# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/3/26 14:09
@File: practice6.py
@Tool: PyCharm 
"""


def scale_n(scalar, vector):
    return tuple(scalar*coord for coord in vector)