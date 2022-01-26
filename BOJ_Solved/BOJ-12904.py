# coding=utf-8
"""
백준 12904번 : A와 B
"""
S = input()
T = input()

if 'A' in S and 'B' in S:
    flag = 1
elif 'A' in S:
    flag = 2
elif 'B' in S:
    flag = 3

while True:
    if T == S:
        print(1)
        break
    else:
        if flag == 1:
            # S에 A와 B 두 개 다 있는 경우
            if 'A' and 'B' in T:
                if T[-1] == 'A':
                    T = T[:-1]
                else:
                    T = T[:-1]
                    T = T[::-1]
            else:
                print(0)
                break
        elif flag == 2:
            # S에 A만 있는 경우
            if 'A' in T:
                if T[-1] == 'A':
                    T = T[:-1]
                else:
                    T = T[:-1]
                    T = T[::-1]
            else:
                print(0)
                break
        elif flag == 3:
            # S에 B만 있는 경우
            if 'B' in T:
                if T[-1] == 'A':
                    T = T[:-1]
                else:
                    T = T[:-1]
                    T = T[::-1]
            else:
                print(0)
                break

