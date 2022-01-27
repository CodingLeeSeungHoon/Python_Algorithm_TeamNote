"""
백준 6497번 : 전력난
- 크루스칼 알고리즘 혹은 프림 알고리즘
"""
import sys
input = sys.stdin.readline

def find(x):
    if Nroot[x] != x:
        Nroot[x] = find(Nroot[x])
    return Nroot[x]


while True:
    M, N = map(int, input().split())
    # 이 포인트가 중요.
    if M == 0 and N == 0:
        break

    Nroot = [i for i in range(M)]
    Elist = []

    for _ in range(N):
        s, e, w = map(int, input().split())
        Elist.append((s, e, w))

    Elist.sort(key=lambda x: x[2])

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

    # 기존은 최소화한 비용 출력, 이번 답은 전체 값 중 아낀 비용 출력
    print(sum(e[2] for e in Elist) - result)