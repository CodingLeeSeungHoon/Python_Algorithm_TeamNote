"""
백준 11728번 : 배열 합치기
"""

_, _ = map(int, input().split())
a = list(map(int, input().split()))
a.extend(list(map(int, input().split())))
print(*sorted(a))