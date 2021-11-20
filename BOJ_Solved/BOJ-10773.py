"""
백준 10773번 : 제로
"""
k = int(input())

money = []

for _ in range(k):
    number = int(input())
    if number == 0:
        del money[len(money) - 1]
    else:
        money.append(number)

print(sum(money))