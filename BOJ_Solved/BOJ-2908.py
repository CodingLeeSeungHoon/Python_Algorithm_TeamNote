"""
백준 2908번 : 상수
"""

a, b = input().split()
print(max(int(a[::-1]), int(b[::-1])))