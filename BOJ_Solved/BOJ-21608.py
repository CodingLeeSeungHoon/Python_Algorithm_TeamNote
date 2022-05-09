"""
백준 21608번 : 상어 초등학교
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
"""
import sys
input = sys.stdin.readline

def check_adjacent(i, j, love):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if classroom[nx][ny] in love:
                cnt += 1

    return cnt

def check_blank(i, j):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if classroom[nx][ny] == 0:
                cnt += 1

    return cnt


N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
classroom = [[0] * N for _ in range(N)]
dict_student = {}

for friends in students:
    student = friends.pop(0)
    dict_student[student] = friends

    best = -1
    best_seat = []

    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                temp = check_adjacent(i, j, friends)
                if best < temp:
                    best = temp
                    best_seat = [[i, j]]
                elif best == temp:
                    best_seat.append([i, j])

    if len(best_seat) == 1:
        i, j = best_seat.pop()
        classroom[i][j] = student
    else:
        adj_blank = -1
        best_blank_seat = []

        for seat in best_seat:
            i, j = seat
            temp = check_blank(i, j)
            if adj_blank < temp:
                adj_blank = temp
                best_blank_seat = [[i, j]]
            elif adj_blank == temp:
                best_blank_seat.append([i, j])

        if len(best_blank_seat) == 1:
            i, j = best_blank_seat.pop()
            classroom[i][j] = student
        else:
            best_blank_seat.sort(key=lambda x: [x[0], x[1]])
            # print(best_blank_seat)
            i, j = best_blank_seat.pop(0)
            classroom[i][j] = student

ans = 0
for i in range(N):
    for j in range(N):
        k = check_adjacent(i, j, dict_student[classroom[i][j]])
        if k != 0:
            ans += 10 ** (k-1)

print(ans)