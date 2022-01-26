# coding=utf-8
"""
백준 1013번 : Contact
"""
import re

T = int(input())
for _ in range(T):
    string = input()
    p = re.compile('(100+1+|01)+')
    result = p.fullmatch(string)
    if result:
        print('YES')
    else:
        print('NO')
