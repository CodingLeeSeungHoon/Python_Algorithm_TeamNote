"""
백준 4673번 : 셀프 넘버
"""

self_number = [True] * 10001
for i in range(1, 10001):
    if sum(map(int, list(str(i)))) + i <= 10000:
        self_number[sum(map(int, list(str(i)))) + i] = False
    if self_number[i]:
        print(i)