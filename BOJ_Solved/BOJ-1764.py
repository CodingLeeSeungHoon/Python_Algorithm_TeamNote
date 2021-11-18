"""
백준 1764번 : 듣보잡
"""

n, m = map(int, input().split())

listen = set()
see = set()

for _ in range(n):
    listen.add(input())

for _ in range(m):
    see.add(input())

s = set(listen) & set(see)
print(len(s))

for i in sorted(s):
    print(i)