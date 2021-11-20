"""
백준 10866번 : 덱
"""
import sys

# input = sys.stdin.readline()

command = int(sys.stdin.readline( ))
deque = []

for _ in range(command):
    c = sys.stdin.readline( ).split( )

    if c[0] == 'push_front':
        deque.insert(0, c[1])
    elif c[0] == 'push_back':
        deque.append(c[1])
    elif c[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)

    elif c[0] == 'pop_back':
        if deque:
            print(deque.pop( ))
        else:
            print(-1)

    elif c[0] == 'size':
        print(len(deque))

    elif c[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)

    elif c[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])

    elif c[0] == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])