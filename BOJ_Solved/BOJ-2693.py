"""
백준 2693번 : N번째 큰 수
"""

T = int(input())
for _ in range(T):
    print(sorted(list(map(int, input().split())), key=lambda x:-x)[2])