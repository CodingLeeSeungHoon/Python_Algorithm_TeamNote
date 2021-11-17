"""
백준 1676번 : 팩토리얼 0의 개수
"""
from math import factorial

n = int(input())
cnt = 0
for i in reversed(str(factorial(n))):
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)