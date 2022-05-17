"""
백준 16204번 : 카드 뽑기
"""

N, M, K = map(int, input().split())
x = N - M
xk = N - K
print(min(M, K) + min(x, xk))