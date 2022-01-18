# coding=utf-8
"""
백준 9461번 : 파도반 수열
"""

dp = [1, 1, 1, 2, 2]

def solution(N):
    if len(dp) >= N:
        return dp[N-1]
    else:
        for i in range(len(dp)-1, N):
            dp.append(dp[i] + dp[i-4])
        return dp[N-1]


T = int(input())

for _ in range(T):
    num = int(input())
    print(solution(num))