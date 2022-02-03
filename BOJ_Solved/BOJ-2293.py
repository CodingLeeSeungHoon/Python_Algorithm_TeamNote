"""
백준 2293번 : 동전 1
"""

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin:
    for j in range(c, k+1):
        if j - c >= 0:
            dp[j] += dp[j-c]

print(dp[k])