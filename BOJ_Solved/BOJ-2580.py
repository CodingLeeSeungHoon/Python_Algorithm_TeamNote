"""
백준 2580번 : 스도쿠
"""
sudoqu = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if sudoqu[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == sudoqu[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == sudoqu[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == sudoqu[nx+i][ny+j]:
                return False
    return True


def solution(idx):
    if idx == len(blank):
        for i in range(9):
            print(*sudoqu[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            sudoqu[x][y] = i
            solution(idx+1)
            sudoqu[x][y] = 0


solution(0)