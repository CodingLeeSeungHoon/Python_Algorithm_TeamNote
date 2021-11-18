"""
백준 11724번 : 연결 요소의 개수
dfs
"""

import sys
from sys import stdin

sys.setrecursionlimit(1000000)

# N : 노드 / M : 간선
N, M = map(int, stdin.readline( ).split( ))
graph = {}
visited = [False] * (N + 1)

for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    end1, end2 = map(int, stdin.readline( ).split( ))
    graph[end1].append(end2)
    graph[end2].append(end1)


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


count = 0
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
