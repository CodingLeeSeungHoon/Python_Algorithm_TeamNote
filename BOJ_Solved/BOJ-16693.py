"""
백준 16693번 : Pizza Deal
"""
import math
a, b = map(int, input().split())
c, d = map(int, input().split())

c = math.pi * (c ** 2)
print('Whole pizza' if b / a > d / c else 'Slice of pizza')