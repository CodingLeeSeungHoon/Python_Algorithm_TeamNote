# coding=utf-8
"""
백준 11727번 : 2xn 타일링 2
"""
N = int(input())

dp = [0, 1, 3, 5]
def solution(N):
    if len(dp) - 1 < N:
        for i in range(len(dp), N+1):
            dp.append(dp[i-1] + 2 * dp[i-2])
    return dp[N]


print(solution(N) % 10007)