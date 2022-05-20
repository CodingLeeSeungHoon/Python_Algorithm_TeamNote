"""
백준 20976번 : The Second Largest Integer
"""

A, B, C = map(int, input().split())
print(sum([A, B, C]) - min([A,B,C]) - max([A,B,C]))