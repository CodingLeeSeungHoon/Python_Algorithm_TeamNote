# coding=utf-8
"""
신발끈 정리
- 2차원 공간에서 좌표가 주어졌을 때 만들어지는 다각형의 면적 구하기
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

print("{}".format(abs(result_a - result_b) / 2))