# coding=utf-8
"""
백준 1780번 : 종이의 개수
"""

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count = []

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x, y, N//3)
                solution(x, y+N//3, N//3)
                solution(x, y+2*N//3, N//3)
                solution(x+N//3, y, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3, y+2*N//3, N//3)
                solution(x+2*N//3, y, N//3)
                solution(x+2*N//3, y+N//3, N//3)
                solution(x+2*N//3, y+2*N//3, N//3)
                return
    if color == -1:
        count.append(-1)
    elif color == 0:
        count.append(0)
    else:
        count.append(1)


solution(0, 0, N)
print(count.count(-1))
print(count.count(0))
print(count.count(1))