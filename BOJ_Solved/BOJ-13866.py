"""
백준 13866번 : 팀 나누기
"""
skill = list(map(int, input().split()))
temp = int(1e9)

for i in range(1, 4):
    other = sum(skill) - skill[0] - skill[i]
    me = skill[0] + skill[i]
    temp = min(abs(other - me), temp)

print(temp)