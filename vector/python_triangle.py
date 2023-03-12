#!/usr/local/bin python
# coding=utf-8
# @Time    : 2023/3/12 13:27
# @Author  : lifangyi
# @File    : python_triangle.py
# @Software: PyCharm


from math import sin, cos, tan, pi, sqrt, pow, atan2

from vectors import length

# 这里面使用的是弧度，而不是角度
r = tan(45)
print(r)

# 45度
r2 = tan(pi/4)
print(r2)

# 极坐标转换为笛卡尔坐标
def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return cos(angle)*length, sin(angle)*length

ag1 = 37*pi/180

ca = to_cartesian((5, ag1))
print(ca)

d=pow(-1.34, 2) + pow(2.68, 2)
fd=sqrt(d)
print(fd)

print(tan((11/90)*pi))

y1 = sin((37/180)*pi)*15
x1 = cos((37/180)*pi)*15
print(x1,y1)


d2=8.5

y2=sin((125/180)*pi)*d2
x2=cos((125/180)*pi)*d2
print(x2, y2)


# 画出一朵花
polar_coord = [(cos(5*x*pi/500), 2*pi*x/10000.0) for x in range(0, 1000)]
ca_vectors = [to_cartesian(p) for p in polar_coord]
# print(ca_vectors)

k = atan2(-1,-5)
print(k)
rk = 2*pi + k
print(rk)

def to_polar(vector):
    x, y = vector[1], vector[0]
    angle = atan2(x, y)
    return length(vector), angle