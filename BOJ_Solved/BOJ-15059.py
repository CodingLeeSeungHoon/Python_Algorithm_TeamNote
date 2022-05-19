"""
백준 15059번 : Hard Choice
"""

a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

ans = 0
ans += 0 if a > d else d-a
ans += 0 if b > e else e-b
ans += 0 if c > f else f-c
print(ans)