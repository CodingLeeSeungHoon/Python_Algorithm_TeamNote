"""
백준 14502번 : 연구소
"""
from itertools import combinations
import copy
from collections import deque
import sys
input = sys.stdin.readline

def bfs(lab, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([x, y])

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < N and 0 <= ny < M:
                if lab[nx][ny] == 0:
                    lab[nx][ny] = 2
                    queue.append([nx, ny])


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
plot = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            plot.append((i, j))


result = -1
for c in combinations(plot, 3):
    lab = copy.deepcopy(graph)
    for p in c:
        x, y = p
        lab[x][y] = 1

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                bfs(lab, i, j)

    temp = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                temp += 1

    result = max(result, temp)

print(result)