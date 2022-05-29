"""
백준 2581번 : 소수
"""

def is_prime(M, N):
    prime = [True] * 10001
    prime[0] = False
    prime[1] = False

    for i in range(2, N):
        for j in range(2*i, N, i):
            prime[j] = False

    return [i for i in range(M, N) if prime[i]]


M = int(input())
N = int(input())
lst = is_prime(M, N+1)

if len(lst) != 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)