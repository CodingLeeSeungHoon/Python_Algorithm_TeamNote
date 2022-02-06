"""
백준 11404번 : 플로이드
- 플로이드-워셜 알고리즘
"""
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = sys.maxsize

G = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())  # 출발 도착 비용
    G[a][b] = min(c, G[a][b])  # 입력보다 더 짧은 노선이 있다면

for k in range(1, n + 1):  # 플로이드 워샬
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                G[i][j] = 0
            else:
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if G[i][j] == INF:  # 경로가 없을시 0으로
            print(0, end=" ")
        else:
            print(G[i][j], end=" ")
    print()
