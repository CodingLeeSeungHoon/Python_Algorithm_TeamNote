"""
백준 2470번 : 두 용액
- 투 포인터
"""
import sys
input = sys.stdin.readline
N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = N - 1

abs_liquid = int(1e11)
result = (-1, -1)
flag = 1

while end > start:
    temp = liquid[start] + liquid[end]
    if temp == 0:
        print("{} {}".format(liquid[start], liquid[end]))
        flag = 0
        break
    elif temp > 0:
        # 양수면 end 한 칸 뒤로 이동
        if abs(temp) < abs_liquid:
            abs_liquid = abs(temp)
            result = (liquid[start], liquid[end])
        end -= 1
    elif temp < 0:
        # 음수면 start 한 칸 앞으로 이동
        if abs(temp) < abs_liquid:
            abs_liquid = abs(temp)
            result = (liquid[start], liquid[end])
        start += 1

if flag:
    print(*result)