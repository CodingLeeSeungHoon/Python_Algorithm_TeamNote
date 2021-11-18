"""
백준 1546번 : 평균
"""
number = int(input( ))
scores = list(map(int, input( ).split( )))

temp = -1

for score in scores:
    if score > temp:
        temp = score

whole = sum(scores)
print((whole * 100 / temp) / number)