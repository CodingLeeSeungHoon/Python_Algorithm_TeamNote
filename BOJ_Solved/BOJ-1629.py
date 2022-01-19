# coding=utf-8
"""
백준 1629번 : 곱셈
분할 정복 이용하기
"""

a, b, c = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % c

    temp = power(a, b // 2)
    if b % 2 == 0:
        # 짝수인 경우
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c


print(power(a, b))
