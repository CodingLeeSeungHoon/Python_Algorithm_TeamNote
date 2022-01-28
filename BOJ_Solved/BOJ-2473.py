"""
백준 2473번 : 세 용액
pypy3로 제출.
투 포인터
"""
import sys
input = sys.stdin.readline

N = int(input())
liquid = sorted(list(map(int, input().split())))

partitial_sum = int(1e10)
result = []

for start in range(N-2):
    mid = start + 1
    end = len(liquid) - 1

    while mid < end:
        temp = liquid[start] + liquid[mid] + liquid[end]
        if abs(partitial_sum) >= abs(temp):
            result = [liquid[start], liquid[mid], liquid[end]]
            partitial_sum = temp

        if temp < 0:
            mid += 1
        elif temp > 0:
            end -= 1
        else:
            print(*result)
            sys.exit()

print(*result)