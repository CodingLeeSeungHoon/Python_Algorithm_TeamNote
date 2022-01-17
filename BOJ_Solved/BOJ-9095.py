# coding=utf-8
"""
백준 9095번 : 1, 2, 3 더하기
"""

T = int(input())
case = [int(input()) for _ in range(T)]

def solution(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 4
    else:
        return solution(number-1) + solution(number-2) + solution(number-3)


for number in case:
    print(solution(number))
