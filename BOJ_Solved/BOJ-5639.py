"""
백준 5639번 : 이진 검색 트리
Binary Search Tree
"""

import sys

sys.setrecursionlimit(10 ** 6)


def postorder(start, end):
    if start > end:
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if post[start] < post[i]:
            division = i
            break

    postorder(start + 1, division - 1)
    postorder(division, end)
    print(post[start])


post = []
count = 0

while True:
    try:
        num = int(input( ))
    except:
        break

    post.append(num)
    count += 1

postorder(0, len(post) - 1)