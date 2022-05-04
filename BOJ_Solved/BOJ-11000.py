"""
백준 11000번 : 강의실 배정
"""

import sys
import heapq

input = sys.stdin.readline
n = int(input())
lessons = [list(map(int, input().split())) for _ in range(n)]

lessons = sorted(lessons, key=lambda x: x[0])

queue = []
for lesson in lessons:
    if queue and queue[0] <= lesson[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, lesson[1])

print(len(queue))