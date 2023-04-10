from collections import deque

def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = deque()
    
    for idx, now in enumerate(numbers):
        if not stack:
            stack.append([idx, now])
            continue
        
        top_idx, top_now = stack[-1]
        while stack and now > top_now:
            stack.pop()
            answer[top_idx] = now
            if stack:
                top_idx, top_now = stack[-1]
        
        stack.append([idx, now])
    
    return answer