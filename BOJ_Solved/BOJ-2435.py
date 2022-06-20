"""
백준 2435번 : 기상청 인턴 신현수
"""

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans_arr = []

for i in range(N-K+1):
    ans_arr.append(sum(arr[i:i+K]))

print(max(ans_arr))