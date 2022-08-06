import sys
input = sys.stdin.readline
N = int(input())
equation = []

for _ in range(N):
    query = list(map(int, input().split()))
    if len(query) == 3:
        _, a, b = query
        if len(equation) == 0:
            equation = [a, b]
        else:
            subs = []
            for idx, e in enumerate(equation):
                equation[idx] = e * a
                subs.append(e * b)
            for idx, s in enumerate(subs):
                if idx != len(subs)-1:
                    equation[idx + 1] += subs[idx]
                else:
                    equation.append(subs[idx])
    else:
        _, x = query
        temp = 0
        for idx, e in enumerate(equation):
            coef = len(equation) - idx - 1
            temp += e * (x ** coef)

        if temp < 0:
            print('-')
        elif temp == 0:
            print(0)
        else:
            print('+')
