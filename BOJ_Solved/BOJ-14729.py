"""
백준 14729번 : 칠무해
"""
import sys

input = sys.stdin.readline
n = int(input())
nums = [0 for _ in range(100001)]

for _ in range(n):
    nums[int("".join(input().split('.')))] += 1

cnt = 7
flag = False
for i in range(100001):
    while nums[i]:
        nums[i] -= 1
        cnt -= 1
        print("{0}.{1:0>3}".format(i//1000, i%1000))
        if cnt == 0:
            flag = True
            break
    if flag:
        break
