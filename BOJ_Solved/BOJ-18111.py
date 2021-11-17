"""
백준 18111번 : 마인크래프트
"""
from sys import stdin

n, m, b = map(int, stdin.readline( ).split( ))
graph = [list(map(int, stdin.readline( ).split( ))) for _ in range(n)]

# 시간, 땅 높이
temp = (10000000000000000000000, 0)
for i in range(257):
    subs = 0  # 쌓으려는 층보다 많은 칸
    adds = 0  # 쌓으려는 층보다 부족한 칸
    for j in range(n):
        for k in range(m):
            if graph[j][k] < i:
                adds += (i - graph[j][k])
            else:
                subs += (graph[j][k] - i)
    inven = subs + b
    if inven < adds:
        continue
    time = 2 * subs + adds
    if time <= temp[0]:
        temp = (time, i)

print("{} {}".format(*temp))