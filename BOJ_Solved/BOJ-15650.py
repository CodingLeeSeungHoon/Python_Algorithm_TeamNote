# coding=utf-8
"""
백준 15650번 : N과 M (2)
"""
from itertools import combinations

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]

for result in list(combinations(num_list, m)):
    print(*result)
