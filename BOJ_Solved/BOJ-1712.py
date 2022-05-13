"""
백준 1712번 : 손익분기점
"""

a, b, c = map(int, input().split())

cnt = 1
if b >= c:
    print(-1)
else:
    cnt = a // (c-b)
    print(cnt + 1)