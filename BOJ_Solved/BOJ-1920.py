"""
백준 1920번 : 수 찾기
이진 탐색 사용!
"""

from bisect import bisect_left

def find(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return 1
    else:
        return 0


m = int(input())
m_line = sorted(list(map(int, input( ).split( ))))

n = int(input())
n_line = list(map(int, input().split()))


for i in n_line:
    print(find(m_line, i))
