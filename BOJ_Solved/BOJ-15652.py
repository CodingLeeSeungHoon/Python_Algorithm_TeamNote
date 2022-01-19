# coding=utf-8
"""
백준 15652번 : N과 M (4)
"""
from itertools import combinations_with_replacement

n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]

for result in combinations_with_replacement(num_list, m):
    print(*result)