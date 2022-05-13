"""
백준 10039번 : 평균 점수
"""

lst = []
for _ in range(5):
    score = int(input())
    if score < 40:
        lst.append(40)
    else:
        lst.append(score)
print(sum(lst)//5)