# coding=utf-8
"""
백준 1389번 : 케빈 베이컨의 6단계 법칙
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1


min_bacon = int(1e9)
result = 0
for i in range(1, N+1):
    visited = [0] * (N + 1)
    bfs(graph, i, visited)
    if min_bacon > sum(visited):
        result = i
        min_bacon = sum(visited)

print(result)