"""
백준 11650번 : 좌표 정렬하기
"""
from sys import stdin

n = int(stdin.readline( ))
points = []

for _ in range(n):
    x, y = map(int, stdin.readline( ).split( ))
    points.append([x, y])

points.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print("{} {}".format(points[i][0], points[i][1]))
