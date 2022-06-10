"""
백준 16134번 : 조합 (Combination)
"""

def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


p = 1000000007
N, K = map(int, input().split())

fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

A = fact[N]
B = (fact[N - K] * fact[K]) % p

print((A % p) * (power(B, p - 2) % p) % p)