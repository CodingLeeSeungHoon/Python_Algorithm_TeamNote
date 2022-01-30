"""
백준 2623번 : 음악프로그램
- 위상정렬
"""
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    sequence = list(map(int, input().split()))
    len_seq = sequence[0]
    seq = sequence[1:]

    for i in range(len_seq - 1):
        graph[seq[i]].append(seq[i+1])
        indegree[seq[i+1]] += 1


queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if indegree.count(0) != N+1:
    print(0)
else:
    for r in result:
        print(r)