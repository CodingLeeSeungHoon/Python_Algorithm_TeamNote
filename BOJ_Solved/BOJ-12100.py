"""
백준 12100번 : 2048(Easy)
"""

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def move(board, idx):
    if idx == 0:
        # up
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[pointer][j] = tmp
        return board
    elif idx == 1:
        # down
        for j in range(n):
            pointer = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
        return board
    elif idx == 2:
        # left
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
        return board
    else:
        # right
        for i in range(n):
            pointer = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
        return board


def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))

    return max(dfs(move(deepcopy(board), 0), cnt + 1),
               dfs(move(deepcopy(board), 1), cnt + 1),
               dfs(move(deepcopy(board), 2), cnt + 1),
               dfs(move(deepcopy(board), 3), cnt + 1))


print(dfs(board, 0))