"""
백준 11948번 : 과목선택
"""
score = []
for _ in range(6):
    score.append(int(input()))

print(sum(score) - min(score[:4]) - min(score[4:]))
