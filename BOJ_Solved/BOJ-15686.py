"""
백준 15686번 : 치킨 배달
"""
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

dist = int(1e9)

for com in combinations(chicken, M):
    dist_temp = 0
    for h in house:
        dist_to_chick = int(1e9)
        hx, hy = h
        for c in com:
            cx, cy = c
            dist_to_chick = min(abs(hx-cx) + abs(hy-cy), dist_to_chick)
        dist_temp += dist_to_chick
    dist = min(dist, dist_temp)

print(dist)