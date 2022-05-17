"""
백준 15921번 : 수찬은 마린보이야!!
"""

N = int(input())
if N != 0:
    score = list(map(int, input().split()))
    ex = 0
    for s in score:
        ex += s / N
    print("{:.2f}".format(round((sum(score)/N)/ex), 3))
else:
    print('divide by zero')