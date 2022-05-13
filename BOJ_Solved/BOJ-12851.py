"""
백준 12851번 : 숨바꼭질 2
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    queue.append(a)
    visited = [-1 for _ in range(100001)]
    visited[a] = 0

    cnt = 0
    while queue:
        me = queue.popleft()
        if me == b:
            cnt += 1

        for y in [me*2, me+1, me-1]:
            if 0 <= y < 100001:
                if visited[y] == -1 or visited[y] >= visited[me] + 1:
                    visited[y] = visited[me] + 1
                    queue.append(y)

    return visited[b], cnt


a, b = map(int, input().split())
time, count = bfs(a, b)
print(time)
print(count)