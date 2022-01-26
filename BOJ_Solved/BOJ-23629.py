# coding=utf-8
"""
백준 23629번 : 이 얼마나 끔찍하고 무시무시한 수식이니
"""

alpha_list = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
num_dict = {alpha_list[i]: str(i) for i in range(10)}
alpha_dict = {str(i): alpha_list[i] for i in range(10)}
alpha_dict['-'] = '-'

flag = 1
expression = input()
symbols = []
num_toint = ''
num_string = ''
numbers = []

for e in expression:
    if e not in '+-=/x':
        num_string += e
        if num_string in num_dict:
            num_toint += num_dict[num_string]
            num_string = ''
    else:
        if num_toint == '':
            print('Madness!')
            flag = 0
            break
        else:
            numbers.append(int(num_toint))
            num_toint = ''
            if e == 'x':
                symbols.append('*')
            else:
                symbols.append(e)


if flag:
    if len(numbers) != len(symbols) or num_toint != '' or num_string != '':
        print('Madness!')
    else:
        result = 0
        for i in range(len(numbers)):
            if i == 0 and symbols[0] == '=':
                result = numbers[0]
            if i == 1:
                if symbols[i-1] == '+':
                    result = numbers[i-1] + numbers[i]
                elif symbols[i-1] == '-':
                    result = numbers[i - 1] - numbers[i]
                elif symbols[i-1] == '*':
                    result = numbers[i - 1] * numbers[i]
                elif symbols[i-1] == '/':
                    result = numbers[i - 1] / numbers[i]
                    if result > 0:
                        result = int(result // 1)
                    else:
                        result = int(result // 1 + 1)
            if i > 1:
                if symbols[i-1] == '+':
                    result += numbers[i]
                elif symbols[i-1] == '-':
                    result -= numbers[i]
                elif symbols[i-1] == '*':
                    result *= numbers[i]
                elif symbols[i-1] == '/':
                    result /= numbers[i]
                    if result > 0:
                        result = int(result // 1)
                    else:
                        result = int(result // 1 + 1)
            print(numbers[i], end='')
            print('x' if symbols[i] == '*' else symbols[i], end='')

        print()
        print("".join(alpha_dict[i] for i in str(result)))
