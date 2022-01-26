# coding=utf-8
"""
백준 1806번 : 부분합
- 투 포인터
"""

N, S = map(int, input().split())
array = list(map(int, input().split()))

length = int(1e9)
interval_sum = 0
end = 0

# start 지점 이동
for start in range(N):
    # end 지점 가능한 만큼 이동
    while interval_sum < S and end < N:
        interval_sum += array[end]
        end += 1
    # 부분합이 S보다 크면 length 비교해 저장
    if interval_sum >= S:
        length = min(length, (end - start))
    interval_sum -= array[start]

if length == int(1e9):
    print(0)
else:
    print(length)