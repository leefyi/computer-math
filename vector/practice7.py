#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/5 15:21
# @Author  : lifangyi
# @File    : practice7.py
# @Software: PyCharm

# 多个向量的加法

def add(*vc):
    return (sum([v[0] for v in vc]), sum([v[1] for v in vc]))

