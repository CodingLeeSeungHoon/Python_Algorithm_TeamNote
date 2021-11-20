"""
백준 2667번 : 단지 번호 붙이기
"""
size = int(input( ))

graph = [[0] * size for i in range(size)]
visited = [[False] * size for i in range(size)]
house_count = []
nums = 0

# graph 채워 넣기
for i in range(size):
    line = input( )
    for j, k in zip(range(size), line):
        if k == '1':
            graph[i][j] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(graph, x, y, visited):
    visited[x][y] = True
    global nums

    if graph[x][y] == 1:
        nums += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # nx와 ny가 0보다 크거나 같은 조건을 넣어줘야 뒤로 넘어가는 일이 없음
        if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(graph, nx, ny, visited)


# 좌표 처음부터 돌아가면서 확인
for i in range(size):
    for j in range(size):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(graph, i, j, visited)
            house_count.append(nums)
            nums = 0

print(len(house_count))
for i in sorted(house_count):
    print(i)