"""
백준 24083번 : 短針 (Hour Hand)
"""

a = int(input())
b = int(input())

print((a+b)%12 if (a+b)%12 != 0 else 12)