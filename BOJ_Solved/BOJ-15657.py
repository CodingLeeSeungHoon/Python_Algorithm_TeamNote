# coding=utf-8
"""
백준 15657번 : N과 M (8)
"""
from itertools import combinations_with_replacement

n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

for result in combinations_with_replacement(num_list, m):
    print(*result)