"""
백준 16395번 : 파스칼의 삼각형
"""

import math
n, k = map(int, input().split())
print(math.comb(n-1, k-1))