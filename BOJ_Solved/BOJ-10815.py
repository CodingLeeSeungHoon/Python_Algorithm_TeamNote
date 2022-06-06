"""
백준 10815번 : 숫자 카드
"""

N = int(input())
dicts = {}
for i in list(map(int, input().split())):
    dicts[i] = 1

M = int(input())
ans = []
for i in list(map(int, input().split())):
    if i not in dicts:
        ans.append(0)
    else:
        ans.append(1)
print(*ans)