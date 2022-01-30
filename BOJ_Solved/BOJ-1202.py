"""
백준 1202번 : 보석 도둑
"""
import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

gemList = [list(map(int, input().split())) for _ in range(N)]
bagList = [int(input()) for _ in range(K)]

gemList.sort()
bagList.sort()

result = 0
temp = []

for bagWeight in bagList:
    while gemList and bagWeight >= gemList[0][0]:
        heapq.heappush(temp, -gemList[0][1])
        heapq.heappop(gemList)

    if temp:
        result += heapq.heappop(temp)
    elif not gemList:
        break

print(-result)