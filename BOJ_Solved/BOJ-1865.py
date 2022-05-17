"""
백준 1865번 : 웜홀
"""

import sys

input = sys.stdin.readline
INF = int(1e9)

# 벨만 포드 알고리즘 응용 -> 최단 거리 알고리즘 x, 그래프상 음의 싸이클 존재 판단 함수
def bf(start):
    dis = [INF] * (n + 1)
    dis[start] = 0

    # 음의 사이클 판별을 위해 n번 반복
    for i in range(n):
        for edge in edges:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]

            # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
            if dis[next_node] > cost + dis[cur]:
                dis[next_node] = cost + dis[cur]
                # i == n-1이면 n번 돌린 상황
                # 이때도 갱신이 발생하면 음의 사이클 존재
                if i == n - 1:
                    return True

    return False


t = int(input())

for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    ans = bf(1)
    if ans:
        print("YES")
    else:
        print("NO")