"""
백준 8674번 : Tabliczka
"""
import math
a, b = map(int, input().split())

a1, a2 = math.floor(a/2), math.ceil(a/2)
b1, b2 = math.floor(b/2), math.ceil(b/2)

print(min(abs(a1*b-a2*b), abs(b1*a-b2*a)))
