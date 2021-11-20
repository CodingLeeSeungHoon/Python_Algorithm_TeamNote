"""
백준 9012번 : 괄호
"""
test = int(input( ))
result = []


def is_vps(ps):
    stack = []

    for p in ps:
        if len(stack) == 0 and p == ')':
            return False
        elif p == ')':
            del stack[len(stack) - 1]
        elif p == '(':
            stack.append(1)

    if len(stack) == 0:
        return True
    else:
        return False


def print_yes_or_no(result):
    for r in result:
        if r == True:
            print('YES')
        else:
            print('NO')


for _ in range(test):
    ps = input( )
    result.append(is_vps(ps))

print_yes_or_no(result)
