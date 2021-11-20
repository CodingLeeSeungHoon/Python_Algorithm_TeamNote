"""
백준 1085번 : 직사각형에서 탈출
"""

x, y, w, h = map(int, input().split())
measure = [x, y, w-x, h-y]
print(min(measure))