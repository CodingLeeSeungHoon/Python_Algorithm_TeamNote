"""
백준 10818번 : 최소, 최대
"""
n = int(input())

num = list(map(int, input().split()))
max_num = max(num)
min_num = min(num)

print("{} {}".format(min_num, max_num))