"""
백준 1021번 : 회전하는 큐
deque에도 rotate 기능이 있다고 함.
"""

from collections import deque

n, m = map(int, input().split())
location = list(map(int, input().split()))

queue = deque([x for x in range(1, n+1)])
count = 0

def get_first_element(queue):
    return queue.popleft()

def move_left(queue):
    queue.append(queue.popleft())

def move_right(queue):
    queue.insert(0, queue.pop())


idx = 0
while True:
    if location[idx] == queue[0]:
        get_first_element(queue)
        idx += 1
    else:
        if queue.index(location[idx]) > len(queue) // 2:
            move_right(queue)
            count += 1
        else:
            move_left(queue)
            count += 1
    if idx == m:
        break


print(count)