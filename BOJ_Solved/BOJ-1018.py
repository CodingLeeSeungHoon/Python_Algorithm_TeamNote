"""
백준 1018번 : 체스판 다시 칠하기
브루트포스 알고리즘
"""
from sys import stdin

n, m = map(int, stdin.readline( ).split( ))

chess1 = [list('WBWBWBWB') if i % 2 == 0 else list('BWBWBWBW') for i in range(8)]
chess2 = [list('BWBWBWBW') if i % 2 == 0 else list('WBWBWBWB') for i in range(8)]

graph = []

for _ in range(n):
    line = list(stdin.readline( ))
    graph.append(line)

temp = 1000000

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for dx in range(8):
            for dy in range(8):
                if graph[i + dx][j + dy] != chess1[dx][dy]:
                    cnt1 += 1
                if graph[i + dx][j + dy] != chess2[dx][dy]:
                    cnt2 += 1
        temp = min(temp, cnt1, cnt2)

print(temp)
