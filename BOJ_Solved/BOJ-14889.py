"""
백준 14889번 : 스타트와 링크
"""
from itertools import combinations

n = int(input())
array = [i for i in range(n)]
matrix = []
for _ in range(n):
    matrix.append((list(map(int, input().split()))))

result = int(1e9)
for r1 in combinations(array, n // 2):
    start, link = 0, 0
    r2 = list(set(array) - set(r1))

    for r in combinations(r1, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]

    for r in combinations(r2, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]

    result = min(result, abs(start - link))
print(result)