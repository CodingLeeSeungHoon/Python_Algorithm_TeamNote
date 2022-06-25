"""
백준 14582번 : 오늘도 졌다
"""

a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = False
sum_a = 0
sum_b = 0
for i in range(9):
    sum_a += a[i]
    if sum_a > sum_b:
        flag = True
        break
    sum_b += b[i]
print('Yes' if flag else 'No')