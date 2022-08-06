"""
백준 1026번 : 보물
"""
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
a.sort()
for i in range(N):
    x = a[i]
    y = b.pop(b.index(max(b)))

    answer += x * y

print(answer)