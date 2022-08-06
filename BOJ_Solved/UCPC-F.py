"""
F번 - Twitch Plays Wlllbit Explorer
"""
from collections import deque

N, M, lenID = map(int, input().split())
item_map = [list(input()) for _ in range(N)]
id = input()
visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(a, b):
    queue = deque()
    queue.append([a, b, "", 0])
    visited[a][b] = True

    # pick, UDLR
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    while queue:
        x, y, log, upgraded = queue.popleft()
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if i == 0 and item_map[nx][ny] == id[len(log)]:
                    log += id[len(log)]
                    item_map[nx][ny]
                    queue.append([nx, ny, log+id[len(log)], ])