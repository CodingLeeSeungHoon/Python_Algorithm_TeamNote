"""
백준 14442번 : 벽 부수고 이동하기 2
"""
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][c]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny][c]:
                    if graph[nx][ny] == 1 and c < K:
                        # 앞이 벽인데 카운트가 K-1보다 작은 경우
                        visited[nx][ny][c+1] = visited[a][b][c] + 1
                        queue.append((nx, ny, c+1))
                    elif graph[nx][ny] == 0:
                        # 앞이 빈 공간, 방문한 적 없음
                        visited[nx][ny][c] = visited[a][b][c] + 1
                        queue.append((nx, ny, c))

    return -1


print(bfs(0, 0, 0))
"""

from collections import deque
queue = deque()
from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
dist = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
graph = [list(map(int, input().strip())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue.append([0, 0, K])
    dist[0][0][K] = 1

    while queue:
        x, y, z = queue.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y][z]

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z > 0 and dist[nx][ny][z - 1] == 0:
                    dist[nx][ny][z - 1] = dist[x][y][z] + 1
                    queue.append([nx, ny, z - 1])
                elif graph[nx][ny] == 0 and dist[nx][ny][z] == 0:
                    dist[nx][ny][z] = dist[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1

print(bfs())