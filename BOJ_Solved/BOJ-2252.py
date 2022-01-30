"""
백준 2252번 : 줄 세우기
- 위상정렬
"""
from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    print(*result)

topology_sort()
