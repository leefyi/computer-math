#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 15:22
# @Author  : lifangyi
# @File    : practice8.py
# @Software: PyCharm

# 为多个向量实现向量平移
from practice7 import add


def translate(translation, vectors):
    result = [add(v,translation) for v in vectors]
    return result