# coding=utf-8
"""
백준 2630번 : 색종이 만들기
"""

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = []


def solution(x, y, N):
    color = paper[x][y]  # 시작점
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


solution(0, 0, N)
print(result.count(0))
print(result.count(1))
