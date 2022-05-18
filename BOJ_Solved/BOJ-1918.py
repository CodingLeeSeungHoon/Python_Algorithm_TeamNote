"""
백준 1918번 : 후위 표기식
"""

text = input()
ans = ''
stack = []

for t in text:
    if t.isalpha():
        ans += t
    else:
        if t == '(':
            stack.append(t)
        elif t == '*' or t == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(t)
        elif t == '+' or t == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()
print(ans)