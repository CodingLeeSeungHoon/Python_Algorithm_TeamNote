"""
백준 9252번 : LCS 2
"""
import sys
input = sys.stdin.readline

first = [0] + list(input().strip())
second = [0] + list(input().strip())

len_f = len(first)
len_s = len(second)

dp = [[""] * len_s for i in range(len_f)]

for i in range(1, len_f):
    for j in range(1, len_s):
        # 인덱스 하나하나 돌아가면서 첫 번째 문자열과 두 번째 문자열의 각 인덱스의 알파벳이 같은지 확인
            if first[i] == second[j]:
                dp[i][j] = dp[i-1][j-1] + first[i]
            else:
                # 알파벳 다르면
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]


print(len(dp[-1][-1]))
print(dp[-1][-1])