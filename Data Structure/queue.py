from collections import deque

queue1 = deque()

# queue 처음 init 할 때, 파라미터로 list 삽입 가능
queue2 = deque([1, 2, 3, 4, 5])

# 삽입 연산
queue2.append()

# 큐 pop 연산
queue2.popleft()
