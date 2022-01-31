"""
백준 1011번 : Fly me to the Alpha Centauri
"""
def solution(x, y):
    # x : 현재 위치, y : 목표 위치
    i = 1
    sub = y - x
    while True:
        if sub - (i**2) >= 0:
            i += 1
        else:
            i -= 1
            break

    rest = sub - (i ** 2)
    if rest > i:
        return i + (i-1) + 2
    if rest == 0:
        return i + (i-1)
    if rest <= i:
        return i + (i-1) + 1


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(solution(x, y))