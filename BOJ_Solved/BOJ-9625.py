"""
백준 9625번 : BABBA
"""

k = int(input())
dpa = [0 for _ in range(46)]
dpb = [0 for _ in range(46)]

dpa[0] = 1

for i in range(1, 46):
    dpa[i] = dpb[i-1]
    dpb[i] = dpb[i-1] + dpa[i-1]

print(dpa[k], dpb[k])

