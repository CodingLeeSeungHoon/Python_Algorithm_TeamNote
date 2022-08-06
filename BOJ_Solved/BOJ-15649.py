"""
백준 15649번 : N과 M (1)
"""

from itertools import permutations
n, m = map(int, input().split())

for c in permutations([i+1 for i in range(n)], m):
    print(*c)