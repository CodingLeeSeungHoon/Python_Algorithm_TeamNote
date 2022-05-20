"""
백준 24294번 : ГРАДИНА
"""

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

print(max(w1, w2) * 2 + (h1+h2) * 2 + 4)