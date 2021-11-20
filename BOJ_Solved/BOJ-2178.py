"""
백준 2178번 : 미로 탐색
bfs
"""
N, M = map(int, input( ).split( ))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [[0] * M for _ in range(N)]

for i in range(N):
    line = input( )
    for j, k in zip(line, range(len(line))):
        if j == '1':
            graph[i][k] = 1


def bfs(graph, x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < N and 0 <= y < M and graph[x][y] == 1:
                queue.append([x, y])
                graph[x][y] = graph[a][b] + 1


bfs(graph, 0, 0)
print(graph[N - 1][M - 1])
