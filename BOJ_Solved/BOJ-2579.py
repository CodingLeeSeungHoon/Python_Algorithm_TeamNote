"""
백준 2579번 : 계단오르기
지옥의 Dynamic Programming
"""

num_stair = int(input())

stair = []
dp = []

for i in range(num_stair):
    stair.append(int(input()))

if num_stair == 1:
    print(stair[0])

elif num_stair == 2:
    dp.append(stair[0])  # 계단 하나만 있는 경우
    dp.append(max(stair[1], stair[1] + stair[0]))  # 계단 2개 한 번에 넘기 vs 계단 둘 다 밟기
    print(dp.pop())

elif num_stair >= 3:
    dp.append(stair[0])  # 계단 하나만 있는 경우
    dp.append(max(stair[1], stair[1] + stair[0]))  # 계단 2개 한 번에 넘기 vs 계단 둘 다 밟기
    dp.append(max(stair[2] + stair[0], stair[2] + stair[1]))  # 마지막 계단은 무조건 밟고, 남은 경우의 수 2가지 중 최대

    for d in range(3, num_stair):
        dp.append(max(stair[d] + dp[d-2], stair[d] + stair[d-1] + dp[d-3]))

    print(dp.pop())
