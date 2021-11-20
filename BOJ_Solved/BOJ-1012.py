"""
백준 1012번 : 유기농 배추
dfs
"""

import sys

sys.setrecursionlimit(10 ** 6)
T = int(input( ))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(graph, y, x, visited):
    visited[y][x] = True  # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and visited[ny][nx] == False:
            dfs(graph, ny, nx, visited)


for _ in range(T):
    M, N, K = map(int, input( ).split( ))

    count = 0
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for k in range(K):
        x, y = map(int, input( ).split( ))
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(graph, i, j, visited)
                count += 1

    print(count)