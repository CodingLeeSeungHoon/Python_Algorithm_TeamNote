"""
백준 14470번 : 전자레인지
"""

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0 < B:
    print(-A * C + B * E + D)

if A < B < 0:
    print((B-A)*C)

if 0 < A < B:
    print((B-A)*E)