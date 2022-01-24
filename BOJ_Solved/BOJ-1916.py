# coding=utf-8
"""
백준 1916번 : 최소비용 구하기
다익스트라 알고리즘
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)
graph = [[] * (N+1) for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    # a : 출발도시 / b : 도착도시 / c : 버스 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

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


dijkstra(start)
print(distance[end])