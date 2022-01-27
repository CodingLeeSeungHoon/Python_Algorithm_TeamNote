"""
백준 1647번 : 도시 분할 계획
- 크루스칼 알고리즘 혹은 프림 알고리즘
"""
import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())

Nroot = [i for i in range(N+1)]
Elist = []
for i in range(M):
    Elist.append(list(map(int, input().split())))
Elist.sort(key=lambda x: x[2])

def find(x):
    if Nroot[x] != x:
        Nroot[x] = find(Nroot[x])
    return Nroot[x]

result = 0
wList = []

for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)

    if sRoot != eRoot:
        if sRoot > eRoot:
            Nroot[sRoot] = eRoot
        else:
            Nroot[eRoot] = sRoot

        result += w
        heapq.heappush(wList, (-w, w))

print(result - heapq.heappop(wList)[1])