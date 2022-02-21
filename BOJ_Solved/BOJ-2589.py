"""
백준 2589번 : 보물섬
"""
from collections import deque
import sys
input = sys.stdin.readline

col, row = map(int, input().split())
maps = [list(input()) for _ in range(col)]

def bfs(a, b, dists):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append([a, b])
    dists[a][b] = 0

    while queue:
        now_a, now_b = queue.popleft()
        for i in range(4):
            na = now_a + dx[i]
            nb = now_b + dy[i]

            if 0 <= na < col and 0 <= nb < row:
                if maps[na][nb] == 'L' and dists[na][nb] == -1:
                    dists[na][nb] = dists[now_a][now_b] + 1
                    queue.append([na, nb])


ans = -1
for i in range(col):
    for j in range(row):
        dists = [[-1] * row for _ in range(col)]
        if maps[i][j] == 'L':
            bfs(i, j, dists)
            for dist in dists:
                ans = max(ans, max(dist))

print(ans)
