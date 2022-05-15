"""
백준 17362번 : 수학은 체육과목 입니다 2
"""
n = int(input())

if n == 1 or (n - 1) % 8 == 0:
    print(1)
elif n == 2 or n == 8 or (n-2) % 8 == 0 or n % 8 == 0:
    print(2)
elif n == 3 or n == 7 or (n-3) % 8 == 0 or (n - 7) % 8 == 0:
    print(3)
elif n == 4 or n == 6 or (n-4) % 8 == 0 or (n - 6) % 8 == 0:
    print(4)
else:
    print(5)