"""
백준 10942번 : 팰린드롬?
"""
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

# 계단형으로 DP 테이블 채우기.
for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len

        if start == end:
            dp[start][end] = 1
        elif numbers[start] == numbers[end]:
            if start + 1 == end:
                # 두 글자 팰린드롬
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                # 양 끝 제외 가운데 문자열이 팰린드롬 -> 팰린드롬
                # dp 테이블 채워 나가는 순서가 계단형이므로 값 존재 보장
                dp[start][end] = 1

for question in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
