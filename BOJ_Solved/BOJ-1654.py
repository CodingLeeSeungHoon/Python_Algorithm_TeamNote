"""
백준 1654번 : 랜선 자르기
이진탐색이지만, bisect 보다 구현하는 것이 답을 해결하기에 좋다.
"""
k, n = map(int, input( ).split( ))
LAN = []
for _ in range(k):
    LAN.append(int(input( )))

start = 1
end = max(LAN)
temp = 0

while start <= end:
    cnt = 0
    mid = (end + start) // 2

    for l in LAN:
        cnt += l // mid

    if cnt >= n:
        if mid > temp:
            temp = mid
        start = mid + 1
    else:
        end = mid - 1

print(temp)