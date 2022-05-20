"""
백준 20233번 : Bicycle
"""

a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

x = 0 if T <= 30 else (T-30)*x*21
y = 0 if T <= 45 else (T-45)*y*21
print(a+x, b+y)