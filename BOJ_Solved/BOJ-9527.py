"""
백준 9527번 : 1의 개수 세기
"""
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
dp = [1]
for i in range(1, 55):
    dp.append((dp[i-1]-1)*2 + 2**(i-1) + 1)

def get_k(num):
    k = 0
    while True:
        if 2 ** k > num:
            return k - 1
        k += 1

def whole_sum(num):
    if num == 1:
        return 1
    if num == 0:
        return 0

    k = get_k(num)
    t = num - (2 ** k)
    return dp[k] + whole_sum(t) + t


print(whole_sum(m) - whole_sum(n - 1))