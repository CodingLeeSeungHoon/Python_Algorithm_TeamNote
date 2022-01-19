# coding=utf-8
"""
백준 1932번 : 정수 삼각형
"""

N = int(input())
pyramid = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    # 층
    for j in range(i+1):
        # 칸
        if j == 0:
            pyramid[i][j] = pyramid[i][j] + pyramid[i-1][j]
        elif j == i:
            pyramid[i][j] = pyramid[i][j] + pyramid[i-1][j-1]
        else:
            pyramid[i][j] = max(pyramid[i][j] + pyramid[i-1][j-1], pyramid[i][j] + pyramid[i-1][j])

print(max(pyramid[-1]))
