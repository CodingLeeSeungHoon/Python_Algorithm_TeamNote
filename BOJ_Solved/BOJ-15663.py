# coding=utf-8
"""
백준 15663번 : N과 M (9)
"""
from itertools import permutations

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

already = {}
for result in permutations(num_list, M):
    if result not in already:
        print(*result)
        already[result] = True
    else:
        continue
