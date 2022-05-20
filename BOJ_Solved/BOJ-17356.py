"""
백준 17356번 : 욱 제
"""
A, B = map(int, input().split())
print(1 / (1 + 10**((B-A)/400)))