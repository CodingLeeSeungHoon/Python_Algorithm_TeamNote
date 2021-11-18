"""
백준 10845번 : 큐
"""
from collections import deque
from sys import stdin

n = int(stdin.readline( ))
queue = deque( )

for i in range(n):
    command = stdin.readline( ).split( )

    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft( ))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)