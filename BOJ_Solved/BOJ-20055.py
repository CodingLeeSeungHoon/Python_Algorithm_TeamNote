"""
백준 20055번 : 컨베이어 벨트 위의 로봇
"""
import sys
input = sys.stdin.readline

def rotate(conveyor, robots):
    ctemp = conveyor.pop()
    conveyor.insert(0, ctemp)

    robots.pop()
    robots.insert(0, 0)

    return conveyor, robots


N, K = map(int, input().split())
conveyor = list(map(int, input().split()))
robots = [0 for _ in range(N)]

stage = 0

while conveyor.count(0) < K:
    conveyor, robots = rotate(conveyor, robots)
    # print("1차 회전 이후 : {}, {}".format(conveyor, robots))

    if robots[-1] == 1:
        robots[-1] = 0

    for i in range(2, N+1):
        if robots[-i] == 1 and conveyor[-N-i+1] != 0 and robots[-i+1] == 0:
            robots[-i] = 0
            robots[-i+1] = 1
            conveyor[-N-i+1] -= 1
        if robots[-1] == 1:
            robots[-1] = 0

    # print("2차 전진 이동 : {}, {}".format(conveyor, robots))

    if robots[0] != 1 and conveyor[0] != 0:
        robots[0] = 1
        conveyor[0] -= 1

    # print("3차 올리는 위치 : {}, {}".format(conveyor, robots))

    stage += 1

print(stage)