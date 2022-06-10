"""
백준 13977번 : 이항 계수와 쿼리
"""

def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b // 2) ** 2 * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


p = 1000000007

m = int(input())
N = []
K = []
for _ in range(m):
    n, k = map(int, input().split())
    N.append(n)
    K.append(k)


fact = [1 for _ in range(max(N) + 1)]

for i in range(2, max(N) + 1):
    fact[i] = fact[i - 1] * i % p

for i in range(m):
    A = fact[N[i]]
    B = (fact[N[i] - K[i]] * fact[K[i]]) % p

    print((A % p) * (power(B, p - 2) % p) % p)