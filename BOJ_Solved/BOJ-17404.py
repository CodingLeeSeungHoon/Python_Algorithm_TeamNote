"""
백준 17404번 : RGB거리 2
조건이 추가된 응용 dp
"""
import sys
input = sys.stdin.readline
N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
ans = INF

# 시작지
for first in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][first] = rgb[0][first]

    # first 선택지에 따라 나머지 경우의 수가 나옴. 나올 수 없는 경우의 수는 INF 이상일 것.
    for j in range(1, N):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        # 시작점과 N번이 같지 않은 결과물만 결과에 반영
        if first != j:
            ans = min(ans, dp[-1][j])

print(ans)