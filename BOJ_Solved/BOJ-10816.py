"""
백준 10816번 : 숫자 카드 2
"""

from collections import Counter

n = int(input())
line = list(map(int, input().split()))

counter = Counter(line)

m = int(input())
m_line = list(map(int, input().split()))

for j in m_line:
    print(counter[j], end=' ')
