"""
백준 15873번 : 공백 없는 A+B
"""

number = input()
if len(number) == 2:
    print(int(number[0]) + int(number[1]))
elif len(number) == 3:
    if number[:2] == '10':
        print(10 + int(number[2]))
    else:
        print(10 + int(number[0]))
else:
    print(20)