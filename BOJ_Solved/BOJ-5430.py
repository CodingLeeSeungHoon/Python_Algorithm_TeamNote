"""
백준 5430번 : AC
"""

from collections import deque

test = int(input( ))

for _ in range(test):
    command = input( )
    len_queue = int(input( ))
    deq = deque(input( ).rstrip( )[1:-1].split(','))
    poss = True
    is_reversed = False

    for c in command:
        if c == 'D' and len_queue == 0:
            print("error")
            poss = False
            break
        elif c == 'D':
            if not is_reversed:
                deq.popleft( )
                len_queue -= 1
            else:
                deq.pop( )
                len_queue -= 1
        elif c == 'R':
            is_reversed = not is_reversed

    if poss:
        if not is_reversed:
            print('[{}]'.format(','.join(deq)))
        else:
            print('[{}]'.format(','.join(deq.pop( ) for _ in range(len_queue))))
