"""
백준 16199번 : 나이 계산하기
"""

by, bm, bd = map(int, input().split())
ny, nm, nd = map(int, input().split())

print(ny-by if nm > bm or (nm == bm and nd >= bd) else ny - by - 1)
print(ny-by+1)
print(ny-by)