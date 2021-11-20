"""
백준 4949번 : 균형잡힌 세상
"""

import sys
lines = sys.stdin.readlines()
for line in lines[:-1]:
    stack = []
    for t in line:
        if t in '([':
            stack.append(t)
        elif t == "]":
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif t == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif t == '.':
            if stack:
                print('no')
            else:
                print("yes")