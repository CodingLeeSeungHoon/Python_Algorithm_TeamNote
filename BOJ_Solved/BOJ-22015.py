"""
백준 22015번 : 金平糖 (Konpeito)
"""

a, b, c = map(int, input().split())
print(max([a, b, c])*3-a-b-c)