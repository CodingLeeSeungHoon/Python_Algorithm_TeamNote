"""
백준 17626번 : Four Squares
Dynamic Programming + pypy3
메모이제이션
"""

n = int(input())

dp = [0, 1]

for i in range(2, n + 1):
    dp.append(dp[i - 1])
    j = 1
    while j ** 2 <= i:
        dp[i] = min(dp[i], dp[i - j ** 2])
        j += 1

    dp[i] += 1

print(dp[n])