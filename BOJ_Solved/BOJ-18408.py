"""
백준 18408번 : 3개의 정수
"""

n = list(map(int, input().split()))
print(1 if n.count(1) > n.count(2) else 2)