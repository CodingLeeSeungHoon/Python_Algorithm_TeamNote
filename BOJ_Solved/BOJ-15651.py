"""
백준 15651번 : N과 M (3)
"""
from itertools import product
N, M = map(int, input().split())

for p in product(range(1, N+1), repeat=M):
    print(*p)