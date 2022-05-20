"""
백준 17874번 : Piece of Cake!
"""

n, v, h = map(int, input().split())
print(max([v*h, (n-v)*(n-h), v*(n-h), h*(n-v)])*4)