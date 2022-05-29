"""
백준 9328번 : 열쇠
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([x, y])
    visited = [[False]*(w+2) for _ in range(h+2)]
    visited[x][y] = True
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if not visited[nx][ny]:
                    if maps[nx][ny] == '.':
                        # 빈 칸
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                    elif maps[nx][ny].islower():
                        # 열쇠 찾았을 때
                        door[ord(maps[nx][ny]) - ord('a')] = 1
                        queue = deque()
                        visited = [[False] * (w + 2) for _ in range(h + 2)]
                        maps[nx][ny] = '.'
                        queue.append([nx, ny])
                    elif maps[nx][ny].isupper():
                        if door[ord(maps[nx][ny])-ord('A')]:
                            # 문을 발견했는 데, 열쇠로 문이 열 수 있을 때
                            visited[nx][ny] = True
                            maps[nx][ny] = '.'
                            queue.append([nx, ny])
                    elif maps[nx][ny] == '$':
                        # 문서를 찾았을 때
                        visited[nx][ny] = True
                        cnt += 1
                        maps[nx][ny] = '.'
                        queue.append([nx, ny])

    print(cnt)


test_case = int(input())
for _ in range(test_case):
    h, w = map(int, input().split())

    # 외곽에 공백 추가
    maps = [['.'] + list(input().strip()) + ['.'] for _ in range(h)]
    maps.insert(0, ['.' for _ in range(w+2)])
    maps.append(['.' for _ in range(w+2)])

    keys = input().rstrip()
    door = [0 for _ in range(26)]

    for k in keys:
        if k != '0':
            door[ord(k) - ord('a')] = 1

    for i in range(h+2):
        for j in range(w+2):
            if ord('A') <= ord(maps[i][j]) <= ord('Z'):
                if door[ord(maps[i][j])-ord('A')]:
                    maps[i][j] = '.'

    bfs(0, 0)

