"""
백준 2133번 : 타일 채우기
"""

N = int(input())
dp = [0 for i in range(31)]
dp[0] = 1

for i in range(2, 31, 2):
    dp[i] = dp[i-2] * 3
    for j in range(0, i-2, 2):
        dp[i] += dp[j] * 2

print(dp[N])