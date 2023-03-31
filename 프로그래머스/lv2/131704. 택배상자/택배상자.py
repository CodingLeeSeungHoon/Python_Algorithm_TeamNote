from collections import deque

def solution(order):
    answer = 0
    container = deque()
    idx = 0
    
    for i in range(1, len(order) + 1):
        container.append(i)
        while container and container[-1] == order[idx]:
            answer += 1
            container.pop()
            idx += 1
        
        
    return answer