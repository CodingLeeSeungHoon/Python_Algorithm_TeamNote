"""
백준 20839번 : Betygsättning
"""

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

if x >= a and y >= b and z >= c:
    print('A')
elif y >= b and z >= c:
    if x >= a/2:
        print('B')
    else:
        print('C')
elif z >= c:
    if y >= b/2:
        print('D')
    else:
        print('E')