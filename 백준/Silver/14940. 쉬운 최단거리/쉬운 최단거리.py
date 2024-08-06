from collections import deque

def oob(nx, ny, n, m):
    return False if 0 <= nx < n and 0 <= ny < m else True

def visited(number):
    return True if number > 0 else False

def is_start_point(x, y, start_point):
    return True if x == start_point[0] and y == start_point[1] else False

def compare(n, m, maps, answer_maps):
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and answer_maps[i][j] == 0:
                answer_maps[i][j] = -1

    return answer_maps

def bfs(n, m, maps, start_point):
    answer_maps = [[0 for _ in range(m)] for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append([start_point[0], start_point[1], 0])
    answer_maps[start_point[0]][start_point[1]] = 0

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not oob(nx, ny, n, m):
                if not visited(answer_maps[nx][ny]) and not is_start_point(nx, ny, start_point):
                    if maps[nx][ny] != 0:
                        queue.append([nx, ny, dist + 1])
                        answer_maps[nx][ny] = dist + 1

    return compare(n, m, maps, answer_maps)


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = []
    start_point = [0, 0]
    for i in range(n):
        line = list(map(int, input().split()))
        if 2 in line:
            start_point = [i, line.index(2)]
        maps.append(line)
    for line in bfs(n, m, maps, start_point):
        print(" ".join(map(str, line)))