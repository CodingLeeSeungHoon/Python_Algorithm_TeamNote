# coding=utf-8
"""
백준 5525번 : IOIOI
"""

N = int(input())
S = int(input())
sentence = input()

indices = []
count = 0
result = 0

for i in range(S):
    if sentence[i] == 'I':
        indices.append(i)

for i in range(len(indices) - 1):
    if indices[i+1] - indices[i] == 2:
        count += 1
    else:
        count = 0

    if count >= N:
        result += 1

print(result)