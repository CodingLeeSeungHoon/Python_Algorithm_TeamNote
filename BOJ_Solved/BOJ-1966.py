"""
백준 1966번 : 프린터 큐
"""
from collections import deque

testcase = int(input( ))

for _ in range(testcase):
    n, m = map(int, input( ).split( ))
    priority = deque(list(map(int, input( ).split( ))))
    queue = deque([0 for i in range(n)])
    queue[m] = 1

    count = 0

    while True:
        if priority[0] == max(priority):
            count += 1
            if queue[0] == 1:
                print(count)
                break
            else:
                priority.popleft( )
                queue.popleft( )
        else:
            priority.append(priority.popleft( ))
            queue.append(queue.popleft( ))
​