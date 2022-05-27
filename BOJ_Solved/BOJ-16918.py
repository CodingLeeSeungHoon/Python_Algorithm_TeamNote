"""
백준 16918번 : 봄버맨
"""

R, C, N = map(int, input().split())
maps = [list(input()) for _ in range(R)]
timer = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'O':
            timer[i][j] = 2

if N == 1:
    for m in maps:
        print("".join(m))
else:
    cnt = 0
    while N != 1:
        N -= 1
        cnt += 1

        if cnt % 2 == 1:
            # 나머지 칸 폭탄 설치
            for i in range(R):
                for j in range(C):
                    if timer[i][j] == 0:
                        timer[i][j] = 4

        for i in range(R):
            for j in range(C):
                if timer[i][j] == 1:
                    timer[i][j] -= 1

                    dx = [-1, 1, 0, 0]
                    dy = [0, 0, 1, -1]

                    for k in range(4):
                        nx = dx[k] + i
                        ny = dy[k] + j

                        if 0 <= nx < R and 0 <= ny < C:
                            if timer[nx][ny] != 1:
                                timer[nx][ny] = 0

                elif timer[i][j] != 0:
                    timer[i][j] -= 1

    for t in timer:
        print(''.join(['O' if n > 0 else '.' for n in t]))