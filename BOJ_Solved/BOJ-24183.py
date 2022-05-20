"""
백준 24183번 : Affischutskicket
"""

a, b, c = map(int, input().split())

e = 229 * 324 * a * 2
p = 297 * 420 * b * 2
i = 210 * 297 * c
print((e+p+i) * 0.000001)