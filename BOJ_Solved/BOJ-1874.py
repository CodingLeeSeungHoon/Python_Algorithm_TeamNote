"""
백준 1874번 : 스택 수열
"""
n = int(input( ))
stack = []
log = []
check = 1
pos = True

for _ in range(n):
    number = int(input( ))
    while check <= number:
        stack.append(check)
        log.append('+')
        check += 1

    if number == stack[-1]:
        stack.pop( )
        log.append('-')
    else:
        pos = False

if pos is False:
    print("NO")
else:
    print("\n".join(log))