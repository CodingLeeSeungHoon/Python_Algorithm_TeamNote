"""
백준 1766번 :  문제집
- 위상정렬
"""
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    now = heapq.heappop(heap)
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end=" ")