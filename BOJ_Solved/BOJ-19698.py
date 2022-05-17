"""
백준 19698번 : 헛간 청약
"""

N, W, H, L = map(int, input().split())
print(min(W//L * H//L, N))