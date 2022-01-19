# coding=utf-8
"""
백준 9465번 : 스티커
"""

T = int(input())
for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    for i in range(N):
        if i == 0:
            continue
        elif i == 1:
            sticker[0][i] = sticker[0][i] + sticker[1][i-1]
            sticker[1][i] = sticker[1][i] + sticker[0][i-1]
        else:
            sticker[0][i] = max(sticker[1][i-1], sticker[1][i-2]) + sticker[0][i]
            sticker[1][i] = max(sticker[0][i-1], sticker[0][i-2]) + sticker[1][i]

    print(max(max(sticker[0]), max(sticker[1])))

