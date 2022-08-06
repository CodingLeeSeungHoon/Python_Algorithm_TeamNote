"""
UCPC-E solved.ac 2022
"""

from datetime import datetime
import sys
input = sys.stdin.readline

def changetime(date, time):
    whole_times = " ".join([date, time])
    answer = datetime.strptime(whole_times, "%Y/%m/%d %H:%M:%S")
    return answer

def getPi(hard_log):
    answer = []
    recent = changetime(hard_log[-1][0], hard_log[-1][1])
    for i in range(1, N+1):
        t = changetime(hard_log[i-1][0], hard_log[i-1][1])
        diff = recent - t
        coef = (diff.days + (diff.seconds/3600/24)) / 365
        answer.append(max(0.5**coef, 0.9**(N-i)))

    return answer

def get_hardness(pi, hard_log):
    hards = [int(hard_log[i][2]) for i in range(N)]
    under = sum(pi)
    upper = sum([hards[i] * pi[i] for i in range(N)])
    return upper/under


N = int(input())
hard_log = []

for _ in range(N):
    date, time, hard = input().split()
    hard_log.append([date, time, hard])

hard_log.sort(key= lambda x:(x[0], x[1]))

# print(hard_log)

if N != 0:
    pi = getPi(hard_log)
    # print(get_hardness(pi, hard_log))
    print(round(get_hardness(pi, hard_log)))
else:
    print(0)
