"""
백준 9019번 : DSLR
"""
from collections import deque

def solution(a, b):
    queue = deque()
    queue.append([a, ''])
    visited = [0 for _ in range(10000)]

    while queue:
        number, log = queue.popleft()
        dtemp = 2 * number % 10000
        if not visited[dtemp]:
            if dtemp == b:
                return log + 'D'
            else:
                visited[dtemp] = 1
                queue.append([dtemp, log + 'D'])

        stemp = 9999 if number - 1 == -1 else number - 1
        if not visited[stemp]:
            if stemp == b:
                return log + 'S'
            else:
                visited[stemp] = 1
                queue.append([stemp, log + 'S'])

        digit_number = (4 - len(str(number))) * '0' + str(number)
        ltemp = int(digit_number[1:] + digit_number[0])
        if not visited[ltemp]:
            if ltemp == b:
                return log + 'L'
            else:
                visited[ltemp] = 1
                queue.append([ltemp, log + 'L'])

        rtemp = int(digit_number[-1] + digit_number[:3])
        if not visited[rtemp]:
            if rtemp == b:
                return log + 'R'
            else:
                visited[rtemp] = 1
                queue.append([rtemp, log + 'R'])


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())
        print(solution(a, b))
