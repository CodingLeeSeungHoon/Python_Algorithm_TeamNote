"""
백준 12852번 : 1로 만들기 2
"""
import sys
input = sys.stdin.readline
N = int(input())
dp = [0 for i in range(N+1)]

if N <= 3:
    for i in range(2, N+1):
        dp[i] = 1
else:
    for i in range(2, 4):
        dp[i] = 1

def solution(N):
    if N > 3:
        if N % 6 == 0:
            dp[N] = min(dp[N//2] + 1, dp[N//3] + 1, dp[N-1] + 1)
            if dp[N] == dp[N//3] + 1:
                return N//3
            if dp[N] == dp[N//2] + 1:
                return N//2
            if dp[N] == dp[N-1] + 1:
                return N-1
        elif N % 3 == 0:
            dp[N] = min(dp[N//3] + 1, dp[N-1] + 1)
            if dp[N] == dp[N//3] + 1:
                return N//3
            if dp[N] == dp[N-1] + 1:
                return N-1
        elif N % 2 == 0:
            dp[N] = min(dp[N//2] + 1, dp[N-1] + 1)
            if dp[N] == dp[N//2] + 1:
                return N//2
            if dp[N] == dp[N-1] + 1:
                return N-1
        else:
            dp[N] = dp[N-1] + 1
            return N-1
    else:
        return 1

for i in range(4, N+1):
    solution(i)
print(dp[N])

temp = N
while temp != 1:
    print(temp, end=" ")
    temp = solution(temp)

print(1)