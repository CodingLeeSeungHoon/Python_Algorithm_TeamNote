"""
프림 알고리즘
- 전체 요소를 연결할 때, 최소 신장 트리를 구성하기 위한 알고리즘
다익스트라 알고리즘과 상당히 유사한 구조를 지닌다. (다익스트라 = 시작점 - 끝점 최소 가중치)
같이 숙지하면 좋다.
"""

import sys
import heapq

input = sys.stdin.readline

# V : vertex / E : edge
V, E = map(int, input().split())

# 방문 여부
visited = [False] * (V + 1)
# 간선 리스트
Elist = [[] for _ in range(V + 1)]

heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    # 시작점 - 끝점, 끝점 - 시작점을 간선 리스트에 넣음. (양방향)
    Elist[s].append([w, e])
    Elist[e].append([w, s])

answer = 0
cnt = 0

# 다익스트라 알고리즘과 유사
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(answer)