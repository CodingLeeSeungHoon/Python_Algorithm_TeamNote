# coding=utf-8
"""
백준 2407번 : 조합
"""

n, m = map(int, input().split())

result = 1
divider = 1

while m != 0:
    result *= n
    divider *= m
    n -= 1
    m -= 1

print(result // divider)