"""
백준 1260번 : DFS와 BFS
dfs, bfs
"""

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        i = queue.popleft( )
        print(i, end=' ')

        for elements in graph[i]:
            if not visited[elements]:
                queue.append(elements)
                visited[elements] = True


n, m, v = map(int, input( ).split( ))
dfs_graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input( ).split( ))
    dfs_graph[i].append(j)
    dfs_graph[j].append(i)

for i in range(1, n + 1):
    dfs_graph[i].sort( )

bfs_graph = dfs_graph[:]

dfs(dfs_graph, v, visited)
visited = [False for _ in range(n + 1)]
print( )
bfs(bfs_graph, v, visited)