"""
백준 15683번 : 감시
"""
from itertools import product
import copy

def confirm(copied_room, i, j, cctv_num, dir_num):
    # 오, 왼, 위, 아래
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def check(direction):
        nx = i
        ny = j
        while True:
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx < N and 0 <= ny < M:
                if copied_room[nx][ny] == 6:
                    break
                if copied_room[nx][ny] == 0:
                    copied_room[nx][ny] = '#'
            else:
                break

    if cctv_num == 1:
        check(dir_num)
    elif cctv_num == 2:
        if dir_num == 0:
            iter = [0, 1]
        else:
            iter = [2, 3]
        for x in iter:
            check(x)
    elif cctv_num == 3:
        if dir_num == 0:
            iter = [0, 3]
        elif dir_num == 1:
            iter = [1, 2]
        elif dir_num == 2:
            iter = [2, 0]
        else:
            iter = [3, 1]

        for x in iter:
            check(x)
    elif cctv_num == 4:
        # 오, 왼, 위, 아래
        if dir_num == 0:
            iter = [0, 3, 1]
        elif dir_num == 1:
            iter = [1, 2, 0]
        elif dir_num == 2:
            iter = [2, 0, 3]
        else:
            iter = [3, 1, 2]

        for x in iter:
            check(x)
    else:
        for x in range(4):
            check(x)


N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cctv = []
kind_cctv = []
comb_cctv = []

for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            cctv.append([i, j])
            kind_cctv.append(room[i][j])

for k in kind_cctv:
    if k == 1:
        comb_cctv.append([i for i in range(4)])
    elif k == 2:
        comb_cctv.append([i for i in range(2)])
    elif k == 3:
        comb_cctv.append([i for i in range(4)])
    elif k == 4:
        comb_cctv.append([i for i in range(4)])
    else:
        comb_cctv.append([0])

ans = int(1e9)
for p in product(*comb_cctv):
    # print(p)
    idx = 0
    new_room = copy.deepcopy(room)
    for i, j in cctv:
        confirm(new_room, i, j, new_room[i][j], p[idx])
        idx += 1

    tmp = 0
    for n in new_room:
        tmp += n.count(0)

    ans = min(ans, tmp)

print(ans)