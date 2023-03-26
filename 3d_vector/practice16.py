# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/3/26 15:10
@File: practice16.py
@Tool: PyCharm 
"""


from math import pi, cos


cv = cos(pi*101.3/180)

dot_uv = 3.61*1.44*cv
print("u和v的点积为：", dot_uv)