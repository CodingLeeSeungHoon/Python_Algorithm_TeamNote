"""
백준 5928번 : Contest Timing
"""

D, H, M = map(int, input().split())
ans = (M + H * 60 + D * 60 * 24) - (11 + 11 * 60 + 11 * 24 * 60)
print(ans if ans >= 0 else -1)