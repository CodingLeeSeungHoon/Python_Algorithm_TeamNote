"""
백준 2231번 : 분해합
"""
natural_number = int(input( ))
result = 0


def is_generator_number(str_num, natural_number):
    length = len(str_num)
    temp = 0
    for index in range(length):
        temp += int(str_num[index])

    temp += int(str_num)

    if temp == natural_number:
        return True
    else:
        return False


for loops in range(1, natural_number + 1):
    if is_generator_number(str(loops), natural_number):
        result = loops
        break

print(result)