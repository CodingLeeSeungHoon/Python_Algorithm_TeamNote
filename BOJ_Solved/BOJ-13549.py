"""
백준 13549번 : 숨바꼭질 3
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    queue.append(a)
    visited = [-1 for _ in range(100001)]
    visited[a] = 0

    while queue:
        me = queue.popleft()
        if me == b:
            return visited[me]

        if 0 <= me-1 < 100001 and visited[me-1] == -1:
            visited[me-1] = visited[me] + 1
            queue.append(me-1)

        if 0 < me * 2 < 100001 and visited[me*2] == -1:
            visited[me*2] = visited[me]
            queue.appendleft(me*2)

        if 0 <= me + 1 < 100001 and visited[me+1] == -1:
            visited[me+1] = visited[me] + 1
            queue.append(me+1)


a, b = map(int, input().split())
print(bfs(a, b))
