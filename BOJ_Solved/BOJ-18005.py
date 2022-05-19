"""
백준 18005번 : Even or Odd?
"""

num = int(input())
if num % 2 == 1:
    print(0)
elif (num // 2) % 2 == 1:
    print(1)
elif (num // 2) % 2 == 0:
    print(2)