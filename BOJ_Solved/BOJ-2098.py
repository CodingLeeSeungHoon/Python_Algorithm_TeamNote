"""
백준 2098번 : 외판원 순회
"""

import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1 << n - 1 == 2**(n-1)
dp = [[0] * (1 << n - 1) for _ in range(n)]

def solution(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (n - 1)) - 1:
        if graph[i][0]:
            return graph[i][0]
        else:
            return 1e9

    bound = 1e9

    for j in range(1, n):
        if not graph[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = graph[i][j] + solution(j, route | (1 << (j - 1)))
        if bound > dist:
            bound = dist
    dp[i][route] = bound

    return bound


print(solution(0, 0))