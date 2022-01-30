"""
백준 2056번 : 작업
- 위상정렬
"""
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]

for i in range(1, N+1):
    command = list(map(int, input().split()))
    # i번 작업을 완료하는데 걸리는 시간
    cost = command[0]
    time[i] = cost

    # 선행작업 개수
    num_before_work = command[1]

    # 선행작업 목록
    before_work = command[2:]

    for b in before_work:
        graph[b].append(i)
        indegree[i] += 1


queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    now = queue.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + time[i], dp[i])
        if indegree[i] == 0:
            queue.append(i)

print(max(dp))
