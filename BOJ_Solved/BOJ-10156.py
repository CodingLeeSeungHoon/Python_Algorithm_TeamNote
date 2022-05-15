"""
백준 10156번 : 과자
"""

K, N, M = map(int, input().split())
ans = K * N - M if K * N - M >= 0 else 0
print(ans)
