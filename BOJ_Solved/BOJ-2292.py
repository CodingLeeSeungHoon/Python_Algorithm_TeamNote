"""
백준 2292번 : 벌집
"""
n = int(input())

cnt = 0
while True:
    if cnt == 0:
        n -= 1
    else:
        n -= 6 * cnt
    cnt += 1
    if n <= 0:
        break

print(cnt)
