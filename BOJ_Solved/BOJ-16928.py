# coding=utf-8
"""
백준 16928번 : 뱀과 사다리 게임
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        for i in range(1, 7):
            y = v + i
            if y > 100:
                continue
            y = graph[y]
            if visited[y] == -1 or visited[y] > visited[v] + 1:
                visited[y] = visited[v] + 1
                queue.append(y)


N, M = map(int, input().split())

graph = [*range(101)]
visited = [-1] * 101

for _ in range(N + M):
    x, y = map(int, input().split())
    graph[x] = y

bfs(graph, 1, visited)
print(visited[-1])

