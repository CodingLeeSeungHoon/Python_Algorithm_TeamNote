"""
백준 1934번 : 최소공배수
"""

def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(LCM(min(a, b), max(a, b)))