"""
백준 1789번 : 수들의 합
"""
N = int(input())
ans = 0
i = 0

while ans < N:
    i += 1
    ans += i

print(i-1 if ans != N else i)