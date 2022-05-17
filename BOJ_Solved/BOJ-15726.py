"""
백준 15726번 : 이칙연산
"""

a, b, c = map(int, input().split())
print(int(max(a/b*c, a*b/c)))