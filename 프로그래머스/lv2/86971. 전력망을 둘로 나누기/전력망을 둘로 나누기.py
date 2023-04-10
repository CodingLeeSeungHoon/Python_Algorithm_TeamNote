import copy
from collections import deque

def bfs(start, tree, n):
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(start)
    visited[start] = True
    result = 1
    
    while queue:
        now = queue.popleft()
        for next_node in tree[now]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                result += 1
                
    return result

def solution(n, wires):
    answer = n
    adjust_arr = [[] for _ in range(n+1)]
    
    for wire in wires:
        a, b = wire
        adjust_arr[a].append(b)
        adjust_arr[b].append(a)
        
    for cut_wire in wires:
        cuta, cutb = cut_wire
        copied_arr = copy.deepcopy(adjust_arr)
        copied_arr[cuta].remove(cutb)
        copied_arr[cutb].remove(cuta)
        
        answer = min(answer, abs(bfs(cuta, copied_arr, n) - bfs(cutb, copied_arr, n)))
        
    return answer