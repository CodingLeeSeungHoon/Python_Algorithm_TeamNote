"""
백준 4386번 : 별자리 만들기
- 크루스칼 알고리즘 혹은 프림 알고리즘
"""
import math
import sys
input = sys.stdin.readline
N = int(input())

star = {}
Nroot = [i for i in range(N+1)]

for i in range(N):
    x, y = map(float, input().split())
    star[i+1] = (x, y)

Elist = []
for i in range(1, N):
    for j in range(i+1, N+1):
        x1, y1 = star[i][0], star[i][1]
        x2, y2 = star[j][0], star[j][1]
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        # print("({} {}) ({} {}) -> dist = {}".format(x1, y1, x2, y2, dist))
        Elist.append([i, j, dist])

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

print(round(result, 2))