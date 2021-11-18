"""
백준 2751번 : 수 정렬하기 2
"""

from sys import stdin

n = int(stdin.readline( ))

number = []
for _ in range(n):
    number.append(int(stdin.readline( )))

number = sorted(number)
print(*number)
