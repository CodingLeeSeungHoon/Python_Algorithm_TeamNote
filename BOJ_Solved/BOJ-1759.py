"""
백준 1759번 : 암호 만들기
"""
from itertools import combinations
import sys
input = sys.stdin.readline

def is_print(word):
    mo = ['a', 'e', 'i', 'o', 'u']
    check_mo = 0
    check_not_mo = 0
    flag = 0

    for w in word:
        if w in mo:
            check_mo += 1
        if w not in mo:
            check_not_mo += 1
        if check_mo >= 1 and check_not_mo >= 2:
            flag = 1
            break

    if flag:
        print("".join(word))


L, C = map(int, input().split())
letter = sorted(list(input().split()))

for c in combinations(letter, L):
    is_print(c)