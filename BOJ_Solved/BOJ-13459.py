"""
백준 13459번 : 구슬 탈출
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
        # print(queue)
        bluex, bluey, redx, redy, move = queue.popleft()
        visited[bluex][bluey][redx][redy] = True

        if move == 10:
            return 0

        for i in range(4):
            nbx = bluex
            nby = bluey
            nrx = redx
            nry = redy

            if i == 0:
                # 위로 기울이기
                if bluex > redx:
                    # 빨간 공이 파란 공보다 위
                    while board[nrx-1][nry] != '#' and board[nrx][nry] != 'O':
                        # 빨간 공 먼저 기울이기
                        nrx -= 1
                    if board[nrx][nry] == 'O':
                        # 빨간 공 구멍에 빠진 상태, 파란 공이 안 빠지면 1, 빠지면 지나가기
                        while board[nbx - 1][nby] != '#' and board[nbx][nby] != 'O':
                            # 파란 공 다음 기울이기
                            nbx -= 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return 1
                    while board[nbx-1][nby] != '#' and board[nbx][nby] != 'O' and (nbx-1 != nrx or nby != nry):
                        # 파란 공 다음 기울이기
                        nbx -= 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    while board[nbx-1][nby] != '#' and board[nbx][nby] != 'O':
                        # 파란 공 먼저 기울이기
                        nbx -= 1
                    if board[nbx][nby] != 'O':
                        while board[nrx - 1][nry] != '#' and board[nrx][nry] != 'O' and (nrx-1 != nbx or nry != nby):
                            # 빨간 공 다음 기울이기
                            nrx -= 1
                        if board[nrx][nry] == 'O':
                            return 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])
            elif i == 1:
                # 아래로 기울이기
                if bluex > redx:
                    # 파란 공이 빨간 공보다 아래
                    while board[nbx+1][nby] != '#' and board[nbx][nby] != 'O':
                        nbx += 1
                    if board[nbx][nby] != 'O':
                        while board[nrx + 1][nry] != '#' and board[nrx][nry] != 'O' and (nrx+1 != nbx or nry != nby):
                            nrx += 1
                        if board[nrx][nry] == 'O':
                            return 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    # 빨간 공이 파란 공보다 아래
                    while board[nrx+1][nry] != '#' and board[nrx][nry] != 'O':
                        nrx += 1
                    if board[nrx][nry] == 'O':
                        # 빨간 공이 구멍에 빠진 상태, 파란 공 빠지면 실패
                        while board[nbx + 1][nby] != '#' and board[nbx][nby] != 'O':
                            nbx += 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return 1
                    while board[nbx+1][nby] != '#' and board[nbx][nby] != 'O' and (nbx+1 != nrx or nby != nry):
                        nbx += 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
            elif i == 2:
                # 오른쪽으로 기울이기
                if bluey > redy:
                    # 파란 공이 빨간 공보다 오른쪽에 있음
                    while board[nbx][nby+1] != '#' and board[nbx][nby] != 'O':
                        nby += 1
                    if board[nbx][nby] != 'O':
                        while board[nrx][nry + 1] != '#' and board[nrx][nry] != 'O' and (nrx != nbx or nry+1 != nby):
                            nry += 1
                        if board[nrx][nry] == 'O':
                            return 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    while board[nrx][nry+1] != '#' and board[nrx][nry] != 'O':
                        nry += 1
                    if board[nrx][nry] == 'O':
                        # 빨간 공 구멍에 빠짐, 파랑공 구멍에 빠지면 실패
                        while board[nbx][nby + 1] != '#' and board[nbx][nby] != 'O':
                            nby += 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return 1
                    while board[nbx][nby+1] != '#' and board[nbx][nby] != 'O' and (nbx != nrx or nby+1 != nry):
                        nby += 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
            elif i == 3:
                # 왼쪽으로 기울이기
                if bluey > redy:
                    # 빨간 공이 파란 공보다 왼쪽에 있음
                    while board[nrx][nry-1] != '#' and board[nrx][nry] != 'O':
                        nry -= 1
                    if board[nrx][nry] == 'O':
                        # 빨간 공 빠짐, 파란 공 빠지면 실패
                        while board[nbx][nby - 1] != '#' and board[nbx][nby] != 'O':
                            nby -= 1
                        if board[nbx][nby] == 'O':
                            continue
                        else:
                            return 1
                    while board[nbx][nby-1] != '#' and board[nbx][nby] != 'O' and (nbx != nrx or nby-1 != nry):
                        nby -= 1
                    if board[nbx][nby] != 'O' and not visited[nbx][nby][nrx][nry]:
                        queue.append([nbx, nby, nrx, nry, move + 1])
                else:
                    # 파란 공이 빨간 공보다 왼쪽에 있음
                    while board[nbx][nby-1] != '#' and board[nbx][nby] != 'O':
                        nby -= 1
                    if board[nbx][nby] != 'O':
                        while board[nrx][nry-1] != '#' and board[nrx][nry] != 'O' and (nrx != nbx or nry-1 != nby):
                            nry -= 1
                        if board[nrx][nry] == 'O':
                            return 1
                        if not visited[nbx][nby][nrx][nry]:
                            queue.append([nbx, nby, nrx, nry, move + 1])

    return 0


print(bfs())