"""
백준 2635번 : 수 이어가기
"""

n = int(input())

ans = -1
ans_array = []

for second in range(1, n+1):
    temp = [n, second]
    init = 1
    while temp[init-1] - temp[init] >= 0:
        temp.append(temp[init-1] - temp[init])
        init += 1

    if ans < init + 1:
        ans = init + 1
        ans_array = temp

print(ans)
print(*ans_array)