"""
백준 5596번 : 시험 점수
"""
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(max(sum(a), sum(b)))