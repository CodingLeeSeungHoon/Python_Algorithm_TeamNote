"""
백준 16236번 : 아기 상어
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j


def biteFish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0

while 1:
    shark = biteFish(x, y, size)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    result += dist
    graph[x][y], graph[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(result)