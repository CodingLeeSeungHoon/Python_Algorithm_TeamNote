"""
백준 16398번 : 행성 연결
- 크루스칼 알고리즘 혹은 프림 알고리즘
"""
import sys
input = sys.stdin.readline
N = int(input())
Nroot = [i for i in range(N)]
Elist = []

flow = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        dist = flow[i][j]
        # print(dist)
        Elist.append((i, j, dist))

Elist.sort(key=lambda x: x[2])

def find(x):
    if Nroot[x] != x:
        Nroot[x] = find(Nroot[x])
    return Nroot[x]


result = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)

    if sRoot != eRoot:
        if sRoot > eRoot:
            Nroot[sRoot] = eRoot
        else:
            Nroot[eRoot] = sRoot
        result += w

print(result)