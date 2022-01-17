# coding=utf-8
"""
백준 1927번 : 최소 힙
"""
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, number)


