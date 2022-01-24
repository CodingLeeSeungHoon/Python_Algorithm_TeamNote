# coding=utf-8
"""
백준 11286번 : 절댓값 힙
"""
import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(heap, (num, num))
    elif num < 0:
        heapq.heappush(heap, (-num, num))
    else:
        if len(heap) == 0:
            print(0)
        else:
            element = heapq.heappop(heap)
            print(element[1])