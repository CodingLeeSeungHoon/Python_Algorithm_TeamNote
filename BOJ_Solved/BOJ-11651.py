"""
백준 11651번 : 좌표 정렬하기 2
"""

n = int(input())

point = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append([x, y])

point.sort(key=lambda x: (x[1], x[0]))
for p in point:
    print("{} {}".format(p[0], p[1]))
