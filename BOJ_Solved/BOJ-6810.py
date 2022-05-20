"""
백준 6810번 : ISBN
"""

ans = 91
a = int(input())
b = int(input())
c = int(input())
print('The 1-3-sum is {}'.format(ans + a + b*3 + c))