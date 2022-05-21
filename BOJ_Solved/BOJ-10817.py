"""
백준 10817번 : 세 수
"""
n = list(map(int, input().split()))
print(sum(n) - max(n) - min(n))