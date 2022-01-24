# coding=utf-8
"""
백준 1238번 : 파티
다익스트라 알고리즘
"""
import heapq
import sys

input = sys.stdin.readline
N, M, X = map(int, input().split())

INF = int(1e9)

graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    # a : start / b : end / t : time
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 인접노드
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


result = -1

for i in range(1, N+1):
    distance = [INF] * (N + 1)
    dijkstra(i)
    go_party = distance[X]

    distance = [INF] * (N + 1)
    dijkstra(X)
    go_home = distance[i]

    result = max(result, go_home + go_party)

print(result)