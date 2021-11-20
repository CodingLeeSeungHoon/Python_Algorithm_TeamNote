"""
백준 1259번 : 펠린드롬 수
"""


def is_pelindrom(number):
    num = str(number)
    length = len(num)

    for i in range(int(length / 2)):
        if num[i] != num[-(i + 1)]:
            return False
    return True


def print_yes_or_no(boolean):
    if boolean:
        print("yes")
    else:
        print("no")


while True:
    number = int(input( ))

    if number != 0:
        print_yes_or_no(is_pelindrom(number))
    else:
        break