"""
백준 24075번 : 計算 (Calculation)
"""

A, B = map(int, input().split())
print(max(A+B, A-B))
print(min(A+B, A-B))