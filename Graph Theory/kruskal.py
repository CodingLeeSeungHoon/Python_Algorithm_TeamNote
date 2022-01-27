"""
크루스칼 알고리즘
- 전체 요소를 연결할 때, 최소 신장 트리를 구성하기 위한 알고리즘
간선이 적을 때 사용하는 것이 유리, 많으면 Prim 알고리즘 사용 권장
"""
import sys
input = sys.stdin.readline

# V : nodes(vertex) / E : edges
V, E = map(int, input().split())

# 연결 요소 중 가장 작은 값, 처음에는 자기 자신을 저장하는 Vroot
Vroot = [i for i in range(V + 1)]

# 간선을 가중치 기준으로 저장 및 정렬
Elist = []
for _ in range(E):
    # input : A번 정점 / B번 정점 / 가중치로 입력이 들어옴.
    Elist.append(list(map(int, input().split())))
Elist.sort(key=lambda x: x[2])


# 간선들이 이은 정점을 찾는 함수
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


answer = 0
for s, e, w in Elist:
    # find 함수를 통해서 두 정점 찾기
    sRoot = find(s)
    eRoot = find(e)

    # 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 한다.
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        # 가중치를 더한다.
        answer += w

print(answer)