# coding=utf-8
"""
백준 2166번 : 다각형의 면적
- 신발끈의 정리
"""
N = int(input())
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

result_a = 0
result_b = 0

for i in range(N):
    if i + 1 != N:
        result_a += X[i]*Y[i+1]
        result_b += X[i+1]*Y[i]
    else:
        result_a += X[i]*Y[0]
        result_b += X[0]*Y[i]

print("{}".format(round((abs(result_a - result_b) / 2), 1)))