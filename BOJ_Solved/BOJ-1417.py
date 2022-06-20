"""
백준 1417번 : 국회의원 선거
"""
import sys
input = sys.stdin.readline

N = int(input())
votes = []
for _ in range(N):
    votes.append(int(input()))

ans = 0
while max(votes) != votes[0] or votes.count(votes[0]) != 1:
    max_temp = -1
    max_idx = -1

    for i in range(1, N):
        if max_temp < votes[i]:
            max_temp = votes[i]
            max_idx = i

    votes[0] += 1
    votes[max_idx] -= 1
    ans += 1

print(ans)