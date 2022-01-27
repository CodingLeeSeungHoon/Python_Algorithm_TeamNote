"""
백준 11779번 : 최소비용 구하기 2
- 다익스트라 알고리즘
"""
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())
path = [[] for _ in range(n+1)]
path[start].append(start)

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

                # 경로 추가
                path[i[0]] = []
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])


dijkstra(start)
print(distance[end])
print(len(path[end]))
print(" ".join(map(str, path[end])))

