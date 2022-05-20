"""
백준 23375번 : Arm Coordination
"""

x, y = map(int, input().split())
r = int(input())

print(x-r, y+r)
print(x+r, y+r)
print(x+r, y-r)
print(x-r, y-r)