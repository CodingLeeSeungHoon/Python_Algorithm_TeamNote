"""
백준 13580번 : Andando no tempo
"""

a, b, c = map(int, input().split())
if a==b or b==c or a==c:
    print('S')
else:
    if a == b+c or b == a+c or c == a+b:
        print('S')
    else:
        print('N')
