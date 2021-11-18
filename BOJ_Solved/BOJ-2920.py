"""
백준 2920번 : 음계
"""

num = list(map(int, input().split()))

ascending = sorted(num)
descending = ascending[::-1]

if num == ascending:
    print('ascending')
elif num == descending:
    print('descending')
else:
    print('mixed')