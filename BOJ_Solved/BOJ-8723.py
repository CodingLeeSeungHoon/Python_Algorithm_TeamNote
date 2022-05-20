"""
백준 8723번 : Patyki
"""

a, b, c = map(int,input().split())
if a == b == c:
    print(2)
elif max(a, b, c) ** 2 == min(a, b, c) ** 2 + (sum([a,b,c])-min(a,b,c)-max(a,b,c)) ** 2:
    print(1)
else:
    print(0)