"""
백준 5635번 : 생일
"""

import sys
input = sys.stdin.readline
n = int(input())
group = []
for _ in range(n):
    name, d, m, y = input().split()
    d, m, y = int(d), int(m), int(y)
    group.append([name, d, m, y])

group = sorted(group, key=lambda x:(x[3], x[2], x[1]))
print(group[-1][0])
print(group[0][0])