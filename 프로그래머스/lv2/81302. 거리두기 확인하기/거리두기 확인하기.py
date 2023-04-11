from collections import deque

def bfs(start, place):
    queue = deque()
    queue.append([start[0], start[1], 0])
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[start[0]][start[1]] = True
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    candidate = []
    
    while queue:
        a, b, dist = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != "X":
                visited[nx][ny] = True
                queue.append([nx, ny, dist + 1])
                if place[nx][ny] == "P":
                    candidate.append(dist + 1)
    
    return True if candidate and min(candidate) <= 2 else False
                

def check_distance(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if bfs([i, j], place):
                    return 0
    return 1
                

def solution(places):
    answer = []
    for place in places:
        answer.append(check_distance(place))
    return answer