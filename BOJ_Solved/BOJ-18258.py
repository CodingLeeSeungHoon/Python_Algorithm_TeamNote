"""
백준 18258번 : 큐 2
"""

from collections import deque
import sys

command = int(sys.stdin.readline( ))
queue = deque([])

for _ in range(command):
    c = sys.stdin.readline( ).split( )

    if c[0] == 'push':
        queue.append(c[1])

    elif c[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif c[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft( ))

    elif c[0] == 'size':
        print(len(queue))

    elif c[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif c[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])