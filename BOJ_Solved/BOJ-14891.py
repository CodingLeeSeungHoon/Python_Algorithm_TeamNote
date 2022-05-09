"""
백준 14891번 : 톱니바퀴
"""
from collections import deque

def rotation(gear, gear_num, direct):
    rotated = [False] * 5
    queue = deque([])
    queue.append([gear_num, direct])
    dx = [1, -1]

    while queue:
        g, d = queue.popleft()
        rotated[g] = True
        front, rear = gear[g-1][2], gear[g-1][6]

        if d == 1:
            # 시계방향
            temp = gear[g-1].pop()
            gear[g-1].insert(0, temp)
        elif d == -1:
            # 반시계방향
            temp = gear[g-1].pop(0)
            gear[g-1].append(temp)

        # print("{}번 기어 {} 방향 회전 : {}".format(g, d, gear))

        for i in range(2):
            nx = dx[i] + g
            if 1 <= nx <= 4 and rotated[nx] is False:
                if nx > g and front != gear[nx-1][6]:
                    if d == 1:
                        queue.append([nx, -1])
                    else:
                        queue.append([nx, 1])
                if nx < g and rear != gear[nx-1][2]:
                    if d == 1:
                        queue.append([nx, -1])
                    else:
                        queue.append([nx, 1])

    return gear


gear = [list(input()) for _ in range(4)]
rotate = int(input())

for _ in range(rotate):
    gear_num, clock = map(int, input().split())
    gear = rotation(gear, gear_num, clock)

print(int(gear[0][0]) + int(gear[1][0])*2 + int(gear[2][0])*4 + int(gear[3][0])*8)
