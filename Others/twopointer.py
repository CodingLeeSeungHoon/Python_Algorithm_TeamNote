# coding=utf-8
"""
- 투 포인터
"""

N, S = map(int, input().split())
array = list(map(int, input().split()))

length = int(1e9)
interval_sum = 0
end = 0

# start 지점 이동 (필수)
for start in range(N):
    # end 지점 가능한 만큼 이동 (필수)
    while interval_sum < S and end < N:
        interval_sum += array[end]
        end += 1
    # 부분합이 S보다 크면 length 비교해 저장
    # 이 부분은 문제의 로직에 따라서 변경
    if interval_sum >= S:
        length = min(length, (end - start))
    # 이 부분을 무조건 적용해야 투 포인터가 완성 (필수)
    interval_sum -= array[start]