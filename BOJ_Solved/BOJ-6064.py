# coding=utf-8
"""
백준 6064번 : 카잉 달력
"""
import sys
input = sys.stdin.readline

def solution(M, N, x, y):
    k = x
    while k <= M * N:
        if (k-x) % M == 0 and (k-y) % N == 0:
            return k
        k += M
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solution(M, N, x, y))