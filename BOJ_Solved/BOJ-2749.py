# coding=utf-8
"""
백준 2749번 : 피보나치 수 3
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
fibonacci = {0: 0, 1: 1, 2: 1}


def getFibonacci(n):
    if not fibonacci.get(n):
        if n % 2 == 1:
            fibonacci[n] = (getFibonacci((n+1)//2)**2 +
                            getFibonacci((n+1)//2-1)**2) % 1000000
        else:
            fibonacci[n] = (getFibonacci(n+1) - getFibonacci(n-1)) % 1000000

    return fibonacci[n]


N = int(input())
print(getFibonacci(N))