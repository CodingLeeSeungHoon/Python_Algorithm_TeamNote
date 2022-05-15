"""
백준 4299번 : AFC 윔블던
"""

hap, cha = map(int, input().split())
a = (hap + cha) / 2
b = a - cha

if hap < cha or a - int(a) > 0:
    print(-1)
else:
    print(int(a), int(b))