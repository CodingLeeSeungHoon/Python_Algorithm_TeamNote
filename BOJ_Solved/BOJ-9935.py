# coding=utf-8
"""
백준 9935번 : 문자열 폭발
"""
string = input()
bomb = input()

lastChar = bomb[-1]
stack = []
length = len(bomb)

for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)