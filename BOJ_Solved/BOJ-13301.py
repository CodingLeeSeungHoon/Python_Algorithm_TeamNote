"""
백준 13301번 : 타일 장식물
"""

tile = [1, 1]

for _ in range(80):
    tile.append(tile[-1] + tile[-2])

n = int(input())
if n == 1:
    print(4)
else:
    print(tile[n-1] * 2 + (tile[n-1] + tile[n-2]) * 2)