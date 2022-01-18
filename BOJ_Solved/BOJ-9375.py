# coding=utf-8
"""
백준 9375번 : 패션왕 신해빈
"""

T = int(input())
for _ in range(T):
    clothes = int(input())
    cloth_dict = {}

    for c in range(clothes):
        element, kind = input().split()
        if kind in cloth_dict:
            cloth_dict[kind].append(element)
        else:
            cloth_dict[kind] = [element]

    count = 1

    for key in cloth_dict:
        count *= (len(cloth_dict[key]) + 1)

    print(count-1)