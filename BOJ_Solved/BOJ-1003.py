"""
백준 1003번 : 피보나치 함수
"""
T = int(input( ))

zero = [1, 0, 1]
one = [0, 1, 1]

for i in range(3, 41):
    zero.append(one[i - 1])
    one.append(one[i - 1] + zero[i - 1])

for _ in range(T):
    number = int(input( ))

    print("{} {}".format(zero[number], one[number]))