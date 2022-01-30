"""
백준 9251번 : LCS
"""
import sys
input = sys.stdin.readline

first = [0] + list(input().strip())
second = [0] + list(input().strip())

len_f = len(first)
len_s = len(second)

dp = [[""] * len_s for _ in range(len_f)]

for i in range(1, len_f):
    for j in range(1, len_s):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + first[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))