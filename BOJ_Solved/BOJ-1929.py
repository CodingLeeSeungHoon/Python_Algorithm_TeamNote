"""
백준 1929번 : 소수 구하기
에라토스테네스의 체
"""

a, b = map(int, input( ).split( ))

def is_prime(a, b):
    prime = [True] * b
    prime[1] = False

    m = int(b ** 0.5)
    for i in range(2, m + 1):
        if prime[i]:
            for j in range(i + i, b, i):
                prime[j] = False

    return [i for i in range(a, b) if prime[i]]


prime = is_prime(a, b + 1)

for p in prime:
    print(p)
