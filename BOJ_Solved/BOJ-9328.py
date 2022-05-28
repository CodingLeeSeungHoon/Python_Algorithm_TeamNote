"""
백준 9328번 : 열쇠
"""


test_case = int(input())
for _ in range(test_case):
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    keys = input()
    start = []

    # 시작점 찾기
    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w):
                if maps[i][j] == '.' or maps[i][j] == '$' or maps[i][j].islower():
                    start.append([i, j])
        else:
            if maps[i][0] == '.' or maps[i][0] == '$' or maps[i][0].islower():
                start.append([i, 0])
            if maps[i][w-1] == '.' or maps[i][w-1] == '$' or maps[i][w-1].islower():
                start.append([i, w-1])
