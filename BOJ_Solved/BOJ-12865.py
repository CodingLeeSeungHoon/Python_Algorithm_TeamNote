"""
백준 12865번 : 평범한 배낭
"""
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = deque()

for _ in range(N):
    w, v = map(int, input().split())
    things.append([w, v])

dp = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N):
    w, v = things.popleft()
    for j in range(K+1):
        if i == 0:
            if j >= w:
                dp[i][j] = v
        else:
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])


print(dp[-1][-1])