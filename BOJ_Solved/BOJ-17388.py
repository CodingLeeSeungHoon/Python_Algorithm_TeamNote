"""
백준 17388번 : 와글와글 숭고한
"""

s, k, h = map(int, input().split())
if s + k + h >= 100:
    print('OK')
else:
    a = min(s, k, h)
    if a == s:
        print('Soongsil')
    elif a == k:
        print('Korea')
    else:
        print('Hanyang')