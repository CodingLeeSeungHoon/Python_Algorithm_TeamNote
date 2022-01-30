"""
백준 2143번 : 두 배열의 합
"""
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
T = int(input())
N = int(input())
A = list(map(int, input().split()))
sum_a = []

M = int(input())
B = list(map(int, input().split()))
sum_b = []

for i in range(N):
    for j in range(i, N):
        temp = sum(A[i:j+1])
        sum_a.append(temp)

for i in range(M):
    for j in range(i, M):
        temp = sum(B[i:j+1])
        sum_b.append(temp)

sum_a.sort()
sum_b.sort()

def counts(a, x):
    # 리스트 내의 원소의 위치 반환, 없으면 에러
    i = bisect_left(a, x)
    j = bisect_right(a, x)
    if i != len(a) and a[i] == x:
        return j-i
    return None

result = 0
if N >= M:
    for value in sum_b:
        temp = counts(sum_a, T-value)
        if temp is not None:
            result += temp
    print(result)
else:
    for value in sum_a:
        temp = counts(sum_b, T-value)
        if temp is not None:
            result += temp
    print(result)