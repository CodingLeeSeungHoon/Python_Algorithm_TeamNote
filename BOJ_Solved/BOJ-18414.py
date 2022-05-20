"""
백준 18414번 : The Nearest Value
"""

X, L, R = map(int, input().split())
before = int(1e9)
ans = -1
for i in range(L, R+1):
    if abs(X-i) < before:
        before = abs(X-i)
    else:
        ans = i-1
        break
if ans == -1:
    print(R)
else:
    print(ans)