# coding=utf-8
"""
백준 1261번 : 알고스팟
"""
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
haze = [[int(i) for i in input() if i != '\n'] for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append([0, 0])
    dist[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if dist[ny][nx] == -1:
                    if haze[ny][nx] == 0:
                        queue.appendleft([nx, ny])
                        dist[ny][nx] = dist[y][x]
                    elif haze[ny][nx] == 1:
                        queue.append([nx, ny])
                        dist[ny][nx] = dist[y][x] + 1


bfs()
print(dist[-1][-1])