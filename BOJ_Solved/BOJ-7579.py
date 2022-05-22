"""
백준 7579번 : 앱
"""

n, m = map(int, input().split())
bytes = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
result = sum(costs)
dp = [[0 for _ in range(result + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    byte = bytes[i]
    cost = costs[i]

    for j in range(1, sum(costs)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

        if m <= dp[i][j]:
            result = min(result, j)

if result != 0:
    print(result)
else:
    print(0)