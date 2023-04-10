from collections import deque
import copy

def bfs(start, ways, visited, n):
    queue = deque()
    queue.append([start, start, visited])
    candidate = []
    
    while queue:
        now, log, visit = queue.popleft()
        if len(log) == 4 * n - 1:
            candidate.append(log)
            continue
        for next in ways[now]:
            visited_key = now + next
            if visit[visited_key] != 0:
                visit[visited_key] -= 1
                queue.append([next, log + " " + next, copy.deepcopy(visit)])
                visit[visited_key] += 1
        
    return sorted(candidate, key = lambda x : x)[0].split(" ")
    
def solution(tickets):
    ways = {}
    visited = {}
    
    for way in tickets:
        start, end = way
        visited_key = start + end
        if visited_key in visited:
            visited[visited_key] += 1
        else:
            visited[visited_key] = 1
            
        if start not in ways:
            ways[start] = [end]
        else:
            ways[start].append(end)
        
        if end not in ways:
            ways[end] = []
    
    return bfs("ICN", ways, visited, len(tickets)+1)
