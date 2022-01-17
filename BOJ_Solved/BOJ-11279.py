# coding=utf-8
"""
백준 11279번 : 최대 힙
"""
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-num, num))  # max_heap

