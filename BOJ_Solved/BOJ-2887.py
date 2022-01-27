"""
백준 16398번 : 행성 터널
- 크루스칼 알고리즘 혹은 프림 알고리즘
"""
import sys
input = sys.stdin.readline
N = int(input())
Nroot = [i for i in range(N)]
planet = []
Elist = []

for i in range(N):
    x, y, z = map(int, input().split())
    planet.append([x, y, z, i])

# 모든 경우의 간선을 구하지 않고, V**2/2
# 좌표 별로 가까운 노드의 간선만을 고른다. 3*(V-1)
for j in range(3):
    # x, y, z 한 번씩 정렬
    planet.sort(key=lambda x: x[j])
    before_planet = planet[0][3]
    for i in range(1, N):
        current_planet = planet[i][3]
        Elist.append([abs(planet[i][j] - planet[i-1][j]), before_planet, current_planet])
        before_planet = current_planet

Elist.sort(key=lambda x: x[0])

def find(x):
    if Nroot[x] != x:
        Nroot[x] = find(Nroot[x])
    return Nroot[x]

result = 0
for w, s, e in Elist:
    sRoot = find(s)
    eRoot = find(e)

    if sRoot != eRoot:
        if sRoot > eRoot:
            Nroot[sRoot] = eRoot
        else:
            Nroot[eRoot] = sRoot
        result += w

print(int(result))