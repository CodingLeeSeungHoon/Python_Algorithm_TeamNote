"""
백준 2606번 : 바이러스
bfs
"""

from collections import deque


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    count = 0
    while queue:
        v = queue.popleft( )
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1

    print(count)


computer = int(input( ))
connected = int(input( ))

graph = [[] for _ in range(computer + 1)]
visited = [False for _ in range(computer + 1)]

for _ in range(connected):
    i, j = map(int, input( ).split( ))
    graph[i].append(j)
    graph[j].append(i)

bfs(graph, 1, visited)