# coding=utf-8
"""
백준 15654번 : N과 M (5)
"""
from itertools import permutations
n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

for result in list(permutations(num_list, m)):
    print(*result)