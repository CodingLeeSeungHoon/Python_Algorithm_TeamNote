"""
백준 1197번 : 최소 스패닝 트리
- 크루스칼 알고리즘 혹은 프림 알고리즘
"""

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

Vroot = [i for i in range(V+1)]
Elist = []

for i in range(E):
    Elist.append(list(map(int, input().split())))
Elist.sort(key=lambda x: x[2]) # 가중치 기준 sort

def find(x):
    if Vroot[x] != x:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


result = 0
for s, e, w in Elist:
    sroot = find(s)
    eroot = find(e)

    if sroot != eroot:
        if sroot > eroot:
            Vroot[sroot] = eroot
        else:
            Vroot[eroot] = sroot

        result += w

print(result)