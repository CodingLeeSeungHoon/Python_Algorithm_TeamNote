"""
백준 24087번 : アイスクリーム (Ice Cream)
"""

s = int(input())
a = int(input())
b = int(input())
cnt = 0

while s > a:
    a += b
    cnt += 1

print(250 + cnt*100)