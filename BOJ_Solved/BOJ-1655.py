"""
백준 1655번 : 가운데를 말해요
- heap을 이용한 실시간 중앙값 찾기
"""
import heapq

N = int(input())
max_heap = []
min_heap = []
answer = []

for i in range(N):
    num = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][0]:
        min = heapq.heappop(min_heap)[0]
        max = heapq.heappop(max_heap)[1]

        heapq.heappush(max_heap, (-min, min))
        heapq.heappush(min_heap, (max, max))

    answer.append(max_heap[0][1])

for j in answer:
    print(j)
