"""
백준 14173번 : Square Pasture
"""

a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

minh, maxh = min(b, d, f, h), max(b, d, f, h)
minw, maxw = min(a, c, e, g), max(a, c, e, g)

print(max(abs(minh-maxh), abs(minw-maxw))**2)