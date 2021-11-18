"""
백준 1157번 : 단어 공부
"""

from collections import Counter

words = input().upper()

counter = Counter(words)
most = counter.most_common(2)


if len(most) == 2 and most[0][1] == most[1][1]:
    print('?')
else:
    print(most[0][0])