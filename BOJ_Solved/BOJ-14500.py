# coding=utf-8
"""
백준 14500번 : 테트로미노
"""
import itertools
import sys

input = sys.stdin.readline
# 세로 : N / 가로 : M
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

result = -1
for j in range(M):
    for i in range(N):
        # i : 세로, j : 가로 / paper[i][j]
        if 0 <= i + 4 <= N:
            # 4x1 폴리노미오
            result = max(result, sum([row[j] for row in paper[i:i+4]]))
        if 0 <= j + 4 <= M:
            # 1x4 폴리노미오
            result = max(result, sum(paper[i][j:j+4]))
        if 0 <= j + 2 <= M and 0 <= i + 2 <= N:
            # 2x2 폴리노미오
            temp = sum(itertools.chain(*[row[j:j+2] for row in paper[i:i+2]]))
            result = max(result, temp)
        if 0 <= i + 3 <= N and 0 <= j + 2 <= M:
            # L 폴리노미오 1
            temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
            result = max(result, temp)
        if 0 <= i + 2 <= N and 0 <= j + 3 <= M:
            # L 폴리노미오 2
            temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j]
            result = max(result, temp)
        if 0 <= i + 3 <= N and 0 <= j + 2 <= M:
            # L 폴리노미오 3
            temp = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]
            result = max(result, temp)
        if 0 <= i - 1 <= N and 0 <= j + 3 <= M:
            # L 폴리노미오 4
            temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i-1][j+2]
            result = max(result, temp)
        if 0 <= i - 2 <= N and 0 <= j + 2 <= M:
            # L 폴리노미오 5
            temp = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-2][j+1]
            result = max(result, temp)
        if 0 <= i + 2 <= N and 0 <= j + 3 <= M:
            # L 폴리노미오 6
            temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]
            result = max(result, temp)
        if 0 <= i + 3 <= N and 0 <= j + 2 <= M:
            # L 폴리노미오 7
            temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i][j+1]
            result = max(result, temp)
        if 0 <= i + 2 <= N and 0 <= j + 3 <= M:
            # L 폴리노미오 8
            temp = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
            result = max(result, temp)
        if 0 <= i + 3 <= N and 0 <= j + 2 <= M:
            # 번개 폴리노미오 1
            temp = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
            result = max(result, temp)
        if 0 <= i - 1 <= N and 0 <= j + 3 <= M:
            # 번개 폴리노미오 2
            temp = paper[i][j] + paper[i][j+1] + paper[i-1][j+1] + paper[i-1][j+2]
            result = max(result, temp)
        if 0 <= i - 2 <= N and 0 <= j + 2 <= M:
            # 번개 폴리노미오 3
            temp = paper[i][j] + paper[i-1][j] + paper[i-1][j+1] + paper[i-2][j+1]
            result = max(result, temp)
        if 0 <= i + 2 <= N and 0 <= j + 3 <= M:
            # 번개 폴리노미오 4
            temp = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2]
            result = max(result, temp)
        if 0 <= i + 2 <= N and 0 <= j + 3 <= M:
            # ㅜ 폴리노미오 1
            temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1]
            result = max(result, temp)
        if 0 <= i + 3 <= N and 0 <= j - 1 <= M:
            # ㅜ 폴리노미오 2
            temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j-1]
            result = max(result, temp)
        if 0 <= i - 1 <= N and 0 <= j + 3 <= M:
            # ㅜ 폴리노미오 3
            temp = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i-1][j+1]
            result = max(result, temp)
        if 0 <= i + 3 <= N and 0 <= j + 2 <= M:
            # ㅜ 폴리노미오 4
            temp = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1]
            result = max(result, temp)

print(result)