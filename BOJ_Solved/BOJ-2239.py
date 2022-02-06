"""
백준 2239번 : 스도쿠
"""

sudoqu = [list(map(int, list(input()))) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if sudoqu[i][j] == 0:
            blank.append((i, j))

def checkRow(x, i):
    for j in range(9):
        if sudoqu[x][j] == i:
            return False
    return True

def checkCol(y, i):
    for j in range(9):
        if sudoqu[j][y] == i:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(nx, nx+3):
        for j in range(ny, ny+3):
            if sudoqu[i][j] == a:
                return False
    return True


def solution(idx):
    if idx == len(blank):
        for s in sudoqu:
            for k in s:
                print(k, end="")
            print()
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            sudoqu[x][y] = i
            solution(idx + 1)
            sudoqu[x][y] = 0


solution(0)