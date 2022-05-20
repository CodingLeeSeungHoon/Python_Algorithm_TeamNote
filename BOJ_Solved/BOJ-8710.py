"""
백준 8710번 : Koszykarz
"""
import math
k, w, m = map(int, input().split())
print(math.ceil((w-k) / m))