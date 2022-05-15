"""
백준 5532번 : 방학 숙제
"""
import math
param = [int(input()) for _ in range(5)]
mat = param[1] / param[3]
kor = param[2] / param[4]

mat = math.ceil(mat)
kor = math.ceil(kor)

print(param[0] - max(mat, kor))