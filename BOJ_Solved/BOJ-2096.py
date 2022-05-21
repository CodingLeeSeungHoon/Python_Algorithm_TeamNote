"""
백준 2096번 : 내려가기
"""
import sys
input = sys.stdin.readline

n = int(input())
minval = [-1, -1, -1]
maxval = [-1, -1, -1]

for i in range(n):
    a, b, c = map(int, input().split())
    if i == 0:
        minval = [a, b, c]
        maxval = [a, b, c]
    else:
        minval = [a+min(minval[0], minval[1]), b+min(minval), c+min(minval[1], minval[2])]
        maxval = [a+max(maxval[0], maxval[1]), b+max(maxval), c+max(maxval[1], maxval[2])]

print(max(maxval), min(minval))