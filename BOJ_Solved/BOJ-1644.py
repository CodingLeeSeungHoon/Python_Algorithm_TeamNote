"""
백준 1644번 : 소수의 연속합
"""

def eratos(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

N = int(input())
prime = eratos(N+1)
prime_len = len(prime)

end = 0
partitial_sum = 0
count = 0

for start in range(prime_len):
    while end < prime_len and partitial_sum < N:
        partitial_sum += prime[end]
        end += 1

    if partitial_sum == N:
        count += 1

    partitial_sum -= prime[start]

print(count)
