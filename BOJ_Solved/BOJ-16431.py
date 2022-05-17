"""
백준 16431번 : 베시와 데이지
"""

bx, by = map(int, input().split())
dx, dy = map(int, input().split())
jx, jy = map(int, input().split())

daisy = abs(jx-dx) + abs(jy-dy)
bessie = 0

ax, ay = abs(bx-jx), abs(by-jy)
if ax >= ay:
    bessie += ax
else:
    bessie += ay

if bessie == daisy:
    print('tie')
elif bessie > daisy:
    print('daisy')
else:
    print('bessie')
