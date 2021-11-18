"""
백준 1978번 : 소수 찾기
"""

n = int(input())
line = list(map(int, input().split()))
high = max(line)
cache = [True] * (high + 1)
cache[0] = False
cache[1] = False

m = int(high ** 0.5)

for i in range(2, m + 1):
    if cache[i]:
        for j in range(i + i, high + 1, i):
            cache[j] = False

cnt = 0
for j in line:
    if cache[j]:
        cnt += 1

print(cnt)
