"""
백준 2206번 : 벽 부수고 이동하기
"""
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])

    while queue:
        a, b, c = queue.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and c == 0:
                    # 앞이 벽, 아직 안 깸
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append([nx, ny, 1])
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    # 앞이 벽 아니고, 방문 안 했으면
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append([nx, ny, c])

    return -1


print(bfs(0, 0, 0))