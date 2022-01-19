# coding=utf-8
"""
백준 15666번 : N과 M (12)
"""
from itertools import combinations_with_replacement

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

already = {}
for result in combinations_with_replacement(num_list, M):
    if result not in already:
        print(*result)
        already[result] = True
    else:
        continue