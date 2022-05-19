"""
백준 13460번 : 구슬 탈출 2
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
bx, by, rx, ry, hx, hy = 0, 0, 0, 0, 0, 0
visited = [[[[False for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            bx, by = i, j
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'O':
            hx, hy = i, j

board[bx][by] = '.'
board[rx][ry] = '.'

def bfs():
    queue = deque()
    queue.append([bx, by, rx, ry, 0])

    while queue:
        bluex, bluey, redx, redy, move = queue.popleft()
        visited[bluex][bluey][redx][redy] = True

        if move == 10:
            return -1

        for i in range(4):
            nbx = bluex
            nby = bluey
            nrx = redx
            nry = redy

            if i == 0:
                if bluex > redx:
                    while board[nrx-1][nry] != '#' and board[nrx][nry] != 'O':
                        nrx -= 1
                    if board[nrx][nry] == 'O':
                        while board[nbx - 1][nby] != '#' and board[nbx][nby] != 'O':
                            nbx -= 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return move + 1
                    while board[nbx-1][nby] != '#' and board[nbx][nby] != 'O' and (nbx-1 != nrx or nby != nry):
                        nbx -= 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    while board[nbx-1][nby] != '#' and board[nbx][nby] != 'O':
                        nbx -= 1
                    if board[nbx][nby] != 'O':
                        while board[nrx - 1][nry] != '#' and board[nrx][nry] != 'O' and (nrx-1 != nbx or nry != nby):
                            nrx -= 1
                        if board[nrx][nry] == 'O':
                            return move + 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])
            elif i == 1:
                if bluex > redx:
                    while board[nbx+1][nby] != '#' and board[nbx][nby] != 'O':
                        nbx += 1
                    if board[nbx][nby] != 'O':
                        while board[nrx + 1][nry] != '#' and board[nrx][nry] != 'O' and (nrx+1 != nbx or nry != nby):
                            nrx += 1
                        if board[nrx][nry] == 'O':
                            return move + 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    while board[nrx+1][nry] != '#' and board[nrx][nry] != 'O':
                        nrx += 1
                    if board[nrx][nry] == 'O':
                        while board[nbx + 1][nby] != '#' and board[nbx][nby] != 'O':
                            nbx += 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return move + 1
                    while board[nbx+1][nby] != '#' and board[nbx][nby] != 'O' and (nbx+1 != nrx or nby != nry):
                        nbx += 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
            elif i == 2:
                if bluey > redy:
                    while board[nbx][nby+1] != '#' and board[nbx][nby] != 'O':
                        nby += 1
                    if board[nbx][nby] != 'O':
                        while board[nrx][nry + 1] != '#' and board[nrx][nry] != 'O' and (nrx != nbx or nry+1 != nby):
                            nry += 1
                        if board[nrx][nry] == 'O':
                            return move + 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    while board[nrx][nry+1] != '#' and board[nrx][nry] != 'O':
                        nry += 1
                    if board[nrx][nry] == 'O':
                        while board[nbx][nby + 1] != '#' and board[nbx][nby] != 'O':
                            nby += 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return move + 1
                    while board[nbx][nby+1] != '#' and board[nbx][nby] != 'O' and (nbx != nrx or nby+1 != nry):
                        nby += 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
            elif i == 3:
                if bluey > redy:
                    while board[nrx][nry-1] != '#' and board[nrx][nry] != 'O':
                        nry -= 1
                    if board[nrx][nry] == 'O':
                        while board[nbx][nby - 1] != '#' and board[nbx][nby] != 'O':
                            nby -= 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return move + 1
                    while board[nbx][nby-1] != '#' and board[nbx][nby] != 'O' and (nbx != nrx or nby-1 != nry):
                        nby -= 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    while board[nbx][nby-1] != '#' and board[nbx][nby] != 'O':
                        nby -= 1
                    if board[nbx][nby] != 'O':
                        while board[nrx][nry-1] != '#' and board[nrx][nry] != 'O' and (nrx != nbx or nry-1 != nby):
                            nry -= 1
                        if board[nrx][nry] == 'O':
                            return move + 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])

    return -1


print(bfs())