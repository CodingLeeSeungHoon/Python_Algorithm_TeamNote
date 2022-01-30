"""
백준 1005번 : ACM Craft
- 위상정렬
"""
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(N+1)]

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(input())
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

    print(dp[W])