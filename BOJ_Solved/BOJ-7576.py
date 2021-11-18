"""
백준 7576번 : 토마토
bfs
"""

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque( )
M, N = map(int, input( ).split( ))

tomato = [[-1] * M for _ in range(N)]

for i in range(N):
    line = list(map(int, input( ).split( )))
    for j, k in zip(line, range(len(line))):
        tomato[i][k] = j
        if j == 1:
            queue.append([i, k])


def bfs(graph):
    while queue:
        a, b = queue.popleft( )

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[a][b] + 1
                    queue.append([nx, ny])


bfs(tomato)
temp = 0
for line in tomato:
    temp = max(temp, max(line))

    if 0 in line:
        print(-1)
        break
    elif line == tomato[len(tomato) - 1]:
        print(temp - 1)
