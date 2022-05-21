"""
백준 24860번 : 항체 계산
"""

v1, j1 = map(int, input().split())
v2, j2 = map(int, input().split())
v3, d3, j3 = map(int, input().split())

print(v3 * d3 * j3 * v1 * j1 + v3 * d3 * j3 * v2 * j2)