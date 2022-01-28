"""
백준 1987번 : 알파벳
- bfs / dfs 인데, set을 이용해서 큐를 만들거나 방문 집합을 만들어줘야 하는 문제
"""
import sys
input = sys.stdin.readline
# R : 세로 / C : 가로
R, C = map(int, input().split())
graph = [input() for _ in range(R)]

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    result = 1
    queue = set([(x, y, graph[0][0])])

    while queue:
        x, y, visited = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < C and 0 <= ny < R:
                if graph[ny][nx] not in visited:
                    next_visited = visited + graph[ny][nx]
                    queue.add((nx, ny, next_visited))
                    result = max(result, len(next_visited))

    return result

print(bfs(0, 0))
