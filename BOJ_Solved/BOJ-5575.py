"""
백준 5575번 : 타임 카드
"""
def solution(array):
    sec = array[5] - array[2]
    min_temp = 0
    if sec < 0:
        sec = 60 + sec
        min_temp = -1

    minute = array[4] - array[1] + min_temp
    hour_temp = 0
    if minute < 0:
        minute = 60 + minute
        hour_temp = - 1

    hour = array[3] - array[0] + hour_temp
    return hour, minute, sec


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in [a, b, c]:
    print(*solution(i))

