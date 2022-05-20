"""
백준 20215번 : Cutting Corners
"""

w, h = map(int, input().split())
d = (w**2 + h**2) ** 0.5
print(w+h - d)