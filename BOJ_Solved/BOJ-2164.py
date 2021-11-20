"""
백준 2164번 : 카드 2
"""

from collections import deque

cards = int(input( ))

queue = deque([i for i in range(1, cards + 1)])
start = 0

while (len(queue) != 1):
    if start % 2 == 0:
        queue.popleft( )
        start += 1
    else:
        temp = queue.popleft( )
        queue.append(temp)
        start += 1

print(queue.popleft( ))
