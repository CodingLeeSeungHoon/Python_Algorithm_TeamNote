"""
백준 3197번 : 백조의 호수
"""
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def can_swan_meet():
    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny]:
                    if lake[nx][ny] == '.':
                        queue.append([nx, ny])
                    else:
                        queue_temp.append([nx, ny])
                    visited[nx][ny] = 1
    return 0


def melt():
    while water_queue:
        x, y = water_queue.popleft()
        if lake[x][y] == 'X':
            lake[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not water_visited[nx][ny]:
                    if lake[nx][ny] == 'X':
                        water_queue_temp.append([nx, ny])
                    else:
                        water_queue.append([nx, ny])
                    water_visited[nx][ny] = 1


if __name__ == "__main__":
    m, n = map(int, input().split())
    visited = [[0] * n for _ in range(m)]
    water_visited = [[0] * n for _ in range(m)]

    lake, swan = [], []
    queue, queue_temp, water_queue, water_queue_temp = deque(), deque(), deque(), deque()

    for i in range(m):
        row = list(input().strip())
        lake.append(row)
        for j, k in enumerate(row):
            if lake[i][j] == 'L':
                swan.extend([i, j])
                water_queue.append([i, j])
            elif lake[i][j] == '.':
                water_visited[i][j] = 1
                water_queue.append([i, j])

    x1, y1, x2, y2 = swan
    queue.append([x1, y1])
    lake[x1][y1], lake[x2][y2], visited[x1][y1] = '.', '.', 1
    cnt = 0

    while True:
        melt()
        if can_swan_meet():
            print(cnt)
            break
        queue, water_queue = queue_temp, water_queue_temp
        queue_temp, water_queue_temp = deque(), deque()
        cnt += 1