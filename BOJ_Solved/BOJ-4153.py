"""
백준 4153번 : 직각 삼각형
"""

while True:
    numbers = list(map(int, input( ).split( )))

    if numbers[0] == numbers[1] == numbers[2] == 0:
        break
    else:
        sqr_num = [x ** 2 for x in numbers]
        biggest = max(sqr_num)
        sqr_num.remove(biggest)
        if biggest == sum(sqr_num):
            print("right")
        else:
            print("wrong")