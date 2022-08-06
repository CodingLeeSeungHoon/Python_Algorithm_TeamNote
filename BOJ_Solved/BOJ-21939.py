"""
백준 21939번 : 문제 추천 시스템 Version 1
"""
import sys
import heapq

input = sys.stdin.readline

maxdic = {}
mindic = {}

num = int(input())
maxheap = []
minheap = []

visit = [False] * 100001

for i in range(num):
    pnum, diff = map(int, input().split(" "))
    heapq.heappush(maxheap, ((-1 * diff), -1 * pnum))
    heapq.heappush(minheap, (diff, pnum))
    visit[pnum] = True
    maxdic[-1 * pnum] = (-1 * diff)
    mindic[pnum] = diff

num = int(input())

for i in range(num):
    command = input().split()
    if command[0] == "add":
        heapq.heappush(maxheap, ((-1*int(command[2])), -1*int(command[1])))
        heapq.heappush(minheap, (int(command[2]), int(command[1])))
        visit[int(command[1])] = True
        maxdic[-1 * int(command[1])] = -1 * int(command[2])
        mindic[int(command[1])] = int(command[2])
    elif command[0] == "recommend" and int(command[1]) == 1:
        while True:
            if visit[-1*maxheap[0][1]] is False :
                heapq.heappop(maxheap)
            elif maxdic[maxheap[0][1]] != maxheap[0][0] :
                heapq.heappop(maxheap)
            else:
                break
        print(-1 * maxheap[0][1])
    elif command[0] == "recommend" and int(command[1]) == -1:
        while True:
            if visit[minheap[0][1]] is False:
                heapq.heappop(minheap)
            elif mindic[minheap[0][1]] != minheap[0][0]:
                heapq.heappop(minheap)
            else:
                break
        print(minheap[0][1])
    else:
        visit[int(command[1])] = False
