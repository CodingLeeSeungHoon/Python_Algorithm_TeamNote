"""
백준 13913번 : 숨바꼭질 4
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    queue.append([a, ""])
    visited = [-1 for _ in range(100001)]
    visited[a] = 0

    while queue:
        me, log = queue.popleft()
        log = log + " " + str(me)

        if me == b:
            return visited[b], log

        for y in [me*2, me+1, me-1]:
            if 0 <= y < 100001:
                if visited[y] == -1:
                    visited[y] = visited[me] + 1
                    queue.append([y, log])


a, b = map(int, input().split())
time, log = bfs(a, b)
print(time)
print(log[1:])