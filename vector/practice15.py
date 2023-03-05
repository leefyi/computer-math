#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 15:32
# @Author  : lifangyi
# @File    : practice15.py
# @Software: PyCharm

# 恐龙图形最长边

from vectors import length

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

def max_l(*vectors):
    ml = 0
    ov = None
    for v in vectors:
        l = length(v)
        if l > ml:
            ml = l
            ov = v
    return ml, ov

ML, rv = max_l(*dino_vectors)
print(ML)
print(rv)

