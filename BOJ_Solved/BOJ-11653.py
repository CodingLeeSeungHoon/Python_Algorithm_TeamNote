"""
백준 11653번 : 소인수분해
"""

N = int(input())
split = []

divider = 2
while True:
    if divider >= N:
        split.append(N)
        break
    if N % divider == 0:
        N = N // divider
        split.append(divider)
    else:
        divider += 1

if N != 1:
    for s in split:
        print(s)