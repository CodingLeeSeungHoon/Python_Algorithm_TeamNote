"""
백준 17470번 : 배열 돌리기 5
"""
import sys
from collections import deque

input = sys.stdin.readline

def rotation(i, deque, flag):
    if i == 1:
        deque.rotate(2)
    elif i == 2:
        deque.reverse()
        deque.rotate(2)
    elif i == 3:
        a, b = deque.popleft(), deque.popleft()
        deque.insert(1, a)
        deque.insert(3, b)
    elif i == 4:
        a = deque.popleft()
        deque.rotate(1)
        b = deque.pop()
        deque.rotate(1)
        deque.append(a)
        deque.append(b)
    elif flag and i == 6:
        a = deque.popleft()
        deque.rotate(1)
        b = deque.pop()
        deque.rotate(1)
        deque.append(a)
        deque.append(b)
    elif flag and i == 5:
        a, b = deque.popleft(), deque.popleft()
        deque.insert(1, a)
        deque.insert(3, b)


N, M, R = map(int, input().split())
half_N = N // 2
half_M = M // 2
arr = [list(map(int, input().split())) for _ in range(N)]

arr_divide = {}
for i in range(4):
    temp = []
    quo = i // 2
    mod = i % 2
    start_x = quo * (N // 2)
    end_x = (quo + 1) * (N // 2)
    start_y = mod * (M // 2)
    end_y = (mod + 1) * (M // 2)
    for x in range(start_x, end_x):
        tmp = []
        for y in range(start_y, end_y):
            tmp.append(arr[x][y])
        temp.append(tmp)
    arr_divide[i + 1] = temp

command_cnt = [0 for _ in range(7)]
command_list = list(map(int, input().split()))

small_list = deque([1, 2, 3, 4])
mini_rotate = deque([0, 1, 2, 3])

for i in command_list:
    rotation(i, small_list, True)
    rotation(i, mini_rotate, False)

position = [[0, 0], [0, M // 2 - 1], [N // 2 - 1, 0], [N // 2 - 1, M // 2 - 1]]
one, two, three = mini_rotate.popleft(), mini_rotate.popleft(), mini_rotate.popleft()

for i in range(4):
    origin = position[one]
    left_origin = position[two]
    bottom_origin = position[three]

    if origin[0] == left_origin[0] and origin[1] == bottom_origin[1]:
        if origin[1] > left_origin[1]:
            dy = -1
        else:
            dy = 1
        if origin[0] > bottom_origin[0]:
            dx = -1
        else:
            dx = 1

        temp = []
        for x in range(abs(bottom_origin[0] - origin[0]) + 1):
            tmp = []
            for y in range(abs(origin[1] - left_origin[1]) + 1):
                tmp.append(arr_divide[i + 1][origin[0] + x * dx][origin[1] + y * dy])
            temp.append(tmp)
        arr_divide[i + 1] = temp
    else:
        if origin[0] > left_origin[0]:
            dy = -1
        else:
            dy = 1

        if origin[1] > bottom_origin[1]:
            dx = -1
        else:
            dx = 1
        temp = []

        for x in range(abs(bottom_origin[1] - origin[1]) + 1):
            tmp = []
            for y in range(abs(left_origin[0] - origin[0]) + 1):
                tmp.append(arr_divide[i + 1][origin[0] + dy * y][origin[1] + dx * x])

            temp.append(tmp)
        arr_divide[i + 1] = temp

last_N = len(arr_divide[1]) * 2
last_M = len(arr_divide[1][0]) * 2

result = [[0 for _ in range(last_M)] for _ in range(last_N)]

for i in range(4):
    idx = small_list.popleft()
    quo = i // 2
    mod = i % 2
    start_x = quo * (last_N // 2)
    start_y = mod * (last_M // 2)
    my_array = arr_divide[idx]
    for x in range(last_N // 2):
        for y in range(last_M // 2):
            result[start_x + x][start_y + y] = my_array[x][y]

for x in range(last_N):
    for y in range(last_M):
        print(result[x][y], end=' ')
    print()
