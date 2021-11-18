"""
백준 4963번 : 섬의 개수
dfs
"""
import sys
sys.setrecursionlimit(5000)

def dfs(i, j):
    # 방문 처리
    graph[i][j] = 0
    dx = [0, 0, 1, -1, 1, -1, -1, 1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for a in range(8):
        x = i + dx[a]
        y = j + dy[a]
        if 0 <= x < h and 0 <= y < w and graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x, y)


while True:
    w, h = map(int, input( ).split( ))
    if w == h == 0:
        break

    graph = []
    for _ in range(h):
        line = list(map(int, input( ).split( )))
        graph.append(line)

    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
