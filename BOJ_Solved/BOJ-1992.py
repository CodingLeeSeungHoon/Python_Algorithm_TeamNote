# coding=utf-8
"""
백준 1992번 : 쿼드트리
"""
import sys
input = sys.stdin.readline

N = int(input())
image = [input() for _ in range(N)]

def solution(x, y, N):
    digit = image[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if image[i][j] != digit:
                print("(", end="")
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                print(")", end="")
                return

    if digit == '1':
        print('1', end="")
    elif digit == '0':
        print('0', end="")


solution(0, 0, N)