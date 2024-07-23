from collections import deque


def oob(x, y, N, M):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False

def bfs(x, y, N, M, campus):
    # 방향
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # 방문 기록
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 첫 포인트 큐에 삽입 + 삽입하면서 체크
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    result = 0

    while queue:
        now_x, now_y = queue.popleft()
        if campus[now_x][now_y] == 'P':
            result += 1
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if oob(nx, ny, N, M):
                if campus[nx][ny] != 'X' and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    campus = list()
    start_point = [-1, -1]

    for i in range(N):
        line = list(input())
        if 'I' in line:
            start_point = [i, line.index('I')]
        campus.append(line)

    result = bfs(start_point[0], start_point[1], N, M, campus)
    print("TT" if result == 0 else result)