"""
백준 17219번 : 비밀번호 찾기
"""

n, m = map(int, input().split())

pw = {}
for _ in range(n):
    site, passwd = input().split()
    pw[site] = passwd

for _ in range(m):
    site = input()
    print(pw[site])