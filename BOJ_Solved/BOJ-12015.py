"""
백준 12015번 : 가장 긴 증가하는 부분 수열 2
"""

from bisect import bisect_left

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))