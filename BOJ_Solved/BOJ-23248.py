# coding=utf-8
"""
백준 23248번 : Treasure Hunter
"""
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
treasure = []

# (x, y) = (가로, 세로)
for _ in range(k):
    x, y = map(int, input().split())
    treasure.append((x, y))

treasure.sort(key=lambda x: (x[1], x[0]))
count = 0

while treasure:
    location = (1, 1)
    plots = []
    time = 0
    size = len(treasure)

    while True:
        if time == size:
            break
        if treasure[0][1] >= location[1] and treasure[0][0] >= location[0]:
            location = treasure[0]
            treasure.pop(0)
        else:
            treasure.append(treasure.pop(0))
        time += 1
    count += 1

print(count)