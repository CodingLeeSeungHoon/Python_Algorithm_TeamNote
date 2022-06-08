"""
백준 1489번 : 뒤집기
"""
cnt = 0
tmp = 'a'
for i in input():
    if tmp != i:
        tmp = i
        cnt += 1
print(cnt // 2)