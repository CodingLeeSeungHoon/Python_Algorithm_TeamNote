N = int(input())
tang = list(map(int, input().split()))

head, tail = 0, 0
stick = [0 for _ in range(10)]
result = 0

while head <= N-1 and tail != N:
    # 탕후루 오른쪽 끝에 과일 삽입 시
    stick[tang[tail]] += 1

    # 두 종류 이하의 과일만 끼웠다면 tail 성공
    if stick.count(0) >= 8:
        result = max(result, sum(stick))
        tail += 1
    else:
        # 두 종류가 넘어간다면, tail을 아직 끼우지 않는다.
        stick[tang[tail]] -= 1
        # 가장 앞의 과일을 빼낸다.
        stick[tang[head]] -= 1
        head += 1

print(result)