"""
백준 3190번 : 뱀
"""
from collections import deque
import sys

input = sys.stdin.readline

def can_rotate(rotation, idx):
    if rotation:
        rotate_time = rotation[0][0]
        if rotate_time == time:
            if rotation[0][1] == 'D':
                idx = (idx + 1) % 4
            if rotation[0][1] == 'L':
                idx = (idx - 1) % 4
            rotation.popleft()
    return idx


n = int(input())
apple = int(input())
maps = [[0 for _ in range(n)] for _ in range(n)]

snake_head = [0, 0]
snake = deque()
snake.append(snake_head)

len_snake = 1
maps[0][0] = 2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(apple):
    i, j = map(int, input().split())
    maps[i-1][j-1] = 1

rotate = int(input())
rotation = deque()
for _ in range(rotate):
    x, c = input().split()
    rotation.append([int(x), c])

time = 0
idx = 0
while True:
    time += 1

    ny = snake_head[0] + dy[idx]
    nx = snake_head[1] + dx[idx]

    if 0 <= nx < n and 0 <= ny < n:
        if maps[ny][nx] == 2:
            # 자기 몸에 부딪힌 경우
            break
        elif maps[ny][nx] == 1:
            # 사과를 만난 경우
            maps[ny][nx] = 2
            snake_head = [ny, nx]
            snake.append([ny, nx])
            idx = can_rotate(rotation, idx)
        else:
            # 비어있는 공간으로 전진한 경우
            maps[ny][nx] = 2
            snake_head = [ny, nx]
            snake.append([ny, nx])
            i, j = snake.popleft()
            maps[i][j] = 0
            idx = can_rotate(rotation, idx)
    else:
        # 벽에 부딪힌 경우
        break

print(time)