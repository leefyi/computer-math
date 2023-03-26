# coding: utf-8

"""
@Author: lifangyi.01
@Time: 2023/3/26 15:12
@File: practice17.py
@Tool: PyCharm
"""


from math import acos

a1 = acos(4 / 5)
a2 = acos(3 / 5)

print(a1, a2)

r1 = a2 - a1
print(r1)
dot_uv = 3 * 4 + 4 * 3

lu = 5
lv = 5

r2 = acos(dot_uv / (lu * lv))
print(r2)
