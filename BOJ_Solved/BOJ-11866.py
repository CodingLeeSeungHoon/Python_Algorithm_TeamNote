"""
백준 11866번 : 요세푸스 문제 0
"""

from collections import deque

n, k = map(int, input( ).split( ))
queue = deque([i for i in range(1, n + 1)])
poped = []

while len(queue) != 0:
    for _ in range(k - 1):
        queue.append(queue.popleft( ))

    poped.append(queue.popleft( ))

print('{}'.format(poped).replace('[', '<').replace(']', '>'))