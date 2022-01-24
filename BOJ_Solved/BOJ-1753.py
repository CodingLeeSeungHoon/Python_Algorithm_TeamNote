# coding=utf-8
"""
백준 1753번 : 최단경로
다익스트라 알고리즘
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

n, m = map(int, input().split())

k = int(input())
INF = int(1e9)

graph = [[] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])