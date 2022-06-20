"""
백준 2638번 : 치즈
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if cheese_map[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                    elif cheese_map[nx][ny] >= 1:
                        cheese_map[nx][ny] += 1


N, M = map(int, input().split())
cheese_map = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    tmp = 0
    for c in cheese_map:
        tmp += sum(c)
    if tmp == 0:
        break

    ans += 1
    bfs()

    for i in range(N):
        for j in range(M):
            if cheese_map[i][j] > 0:
                if cheese_map[i][j] >= 3:
                    cheese_map[i][j] = 0
                else:
                    cheese_map[i][j] = 1

print(ans)