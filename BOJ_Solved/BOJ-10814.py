"""
백준 10814번 : 나이순 정렬
"""
from sys import stdin

n = int(stdin.readline( ))

person = []
for i in range(n):
    data = stdin.readline( ).split( )
    person.append([int(data[0]), data[1], i])

person.sort(key=lambda x: (x[0], x[2]))

for p in person:
    print("{} {}".format(p[0], p[1]))
