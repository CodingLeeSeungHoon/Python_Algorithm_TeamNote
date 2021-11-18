"""
백준 2577번 : 숫자의 개수
"""

from collections import Counter

number = 1
for _ in range(3):
    number *= int(input( ))

counter = Counter(str(number))
for i in [str(k) for k in range(10)]:
    if i not in counter:
        print(0)
    else:
        print(counter[i])
