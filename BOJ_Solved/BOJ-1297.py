"""
백준 1297번 : TV 크기
"""
d, h, w = map(int, input().split())
daegak = (h ** 2 + w ** 2) ** 0.5

base = d / daegak
print(int(base * h), int(base * w))