# coding=utf-8
"""
백준 16953번 : A -> B
"""

A, B = map(int, input().split())
count = 0

while A < B:
    string = str(B)
    if str(B)[-1] == '1':
        B = int(string[:len(string)-1])
        count += 1
    else:
        if B % 2 == 0:
            B = B // 2
            count += 1
        else:
            break

if A == B:
    print(count + 1)
else:
    print(-1)