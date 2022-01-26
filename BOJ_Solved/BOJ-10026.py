# coding=utf-8
"""
백준 10026번 : 적록색약
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs_normal(start, count):
    # start = [x, y]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if dist[start[0]][start[1]] != -1:
        return -1

    x, y = start[0], start[1]
    queue = deque()
    queue.append([x, y])
    dist[x][y] = count
    color = image[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1:
                    if image[nx][ny] == color:
                        queue.append([nx, ny])
                        dist[nx][ny] = count

    return 1


def bfs_redgreen(start, count):
    # start = [x, y]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if dist[start[0]][start[1]] != -1:
        return -1

    flag = 0
    x, y = start[0], start[1]
    queue = deque()
    queue.append([x, y])
    dist[x][y] = count
    color = image[x][y]
    if color == 'R' or color == 'G':
        flag = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1:
                    if flag:
                        if image[nx][ny] == 'R' or image[nx][ny] == 'G':
                            queue.append([nx, ny])
                            dist[nx][ny] = count
                    else:
                        if image[nx][ny] == color:
                            queue.append([nx, ny])
                            dist[nx][ny] = count

    return 1


if __name__ == "__main__":
    N = int(input())
    image = [input() for _ in range(N)]
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    count = 1
    for i in range(N):
        for j in range(N):
            if bfs_normal([i, j], count) != -1:
                count += 1

    print(max(map(max, *dist)), end=" ")

    dist = [[-1 for _ in range(N)] for _ in range(N)]
    count = 1
    for i in range(N):
        for j in range(N):
            if bfs_redgreen([i, j], count) != -1:
                count += 1

    print(max(map(max, *dist)), end="")