"""
백준 2805번 : 나무 자르기
이분 탐색으로 해결하기~!
"""
from sys import stdin

n, m = map(int, stdin.readline().split())

trees = list(map(int, stdin.readline( ).split( )))
start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    # list comprehension으로 풀지 않으면 시간 오류
    cnt = sum(t - mid if t > mid else 0 for t in trees)

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)