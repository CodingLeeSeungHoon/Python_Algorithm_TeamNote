"""
백준 2775번 : 부녀회장이 될테야
"""
test = int(input())

for _ in range(test):
    floor = int(input())  # 층
    home = int(input())  # 호

    apart = [i for i in range(1, home + 1)]
    for k in range(floor):
        for n in range(1, home):
            apart[n] += apart[n - 1]

    print(apart[-1])
