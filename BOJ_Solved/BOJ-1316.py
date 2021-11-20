"""
백준 1316번 : 그룹 단어 체커
"""

import sys

n = int(input( ))
count = 0

for _ in range(n):
    word = sys.stdin.readline( )
    letter = []
    before = -1
    for i in word:
        if i == before or i not in letter:
            letter.append(i)
            before = i
        else:
            before = -1
            break

    if before != -1:
        count += 1

print(count)