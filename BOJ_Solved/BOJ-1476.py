"""
백준 1476번 : 날짜 계산
"""

E, S, M = map(int, input().split())
a, b, c = 1, 1, 1
ans = 1
while E != a or S != b or M != c:
    ans += 1
    a += 1
    b += 1
    c += 1
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
print(ans)