"""
백준 11383번 : 뚊
"""

N, M = map(int, input().split())
first = []
second = []

for _ in range(N):
    first.append(input())

for _ in range(N):
    second.append(input())

flag = 1
for i in range(N):
    a = first[i]
    b = second[i]

    string = ""
    for j in a:
        string += j
        string += j

    if string != b:
        flag = 0

if flag:
    print("Eyfa")
else:
    print("Not Eyfa")