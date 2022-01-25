# coding=utf-8
"""
백준 7569번 : 토마토
"""
from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs():
    queue = deque()
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    # 토마토가 익은 상태인 것 찾기
                    queue.append([i, j, k])

    while queue:
        x = queue.popleft()
        for i in range(6):
            if 0 <= x[0]+dx[i] < H and 0 <= x[1]+dy[i] < N and 0 <= x[2]+dz[i] < M:
                if tomato[x[0]+dx[i]][x[1]+dy[i]][x[2]+dz[i]] == 0:
                    queue.append((x[0] + dx[i], x[1]+dy[i], x[2]+dz[i]))
                    tomato[x[0] + dx[i]][x[1] + dy[i]][x[2] + dz[i]] = tomato[x[0]][x[1]][x[2]] + 1


bfs()
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                day = max(day, tomato[i][j][k])

print(day-1)
