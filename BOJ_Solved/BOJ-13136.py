"""
백준 13136번 : Do Not Touch Anything
"""
import math
R, C, N = map(int, input().split())
print(int(math.ceil(R/N) * math.ceil(C/N)))