# coding=utf-8
"""
백준 11726번 : 2xn 타일링
"""
import sys
sys.setrecursionlimit(10**6)

n = int(input())

dp = [0, 1, 2]

def solution(n):
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])


solution(n)
print(dp[n] % 10007)
