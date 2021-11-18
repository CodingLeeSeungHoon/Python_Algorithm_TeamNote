"""
백준 2739번 : 구구단
"""

num = int(input())

for i in range(1, 10):
    print("{} * {} = {}".format(num, i, num*i))
