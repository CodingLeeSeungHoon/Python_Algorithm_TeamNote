"""
백준 2441번 : 별 찍기 - 4
"""
n = int(input())
a = n
while n != 0:
    print(' '*(a-n), end='')
    print('*'*n)
    n-=1