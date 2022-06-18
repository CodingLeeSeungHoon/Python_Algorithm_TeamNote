"""
백준 7490번 : 0 만들기
"""

import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    operators_list = []
    recursive([], n - 1)
    integer = [i for i in range(1, n+1)]

    for operator in operators_list:
        string = ""
        for i in range(n-1):
            string += str(integer[i]) + operator[i]
        string += str(integer[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()