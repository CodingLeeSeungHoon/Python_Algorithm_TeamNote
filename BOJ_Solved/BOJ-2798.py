"""
백준 2798번 : 블랙잭
"""

cards_info = list(map(int, input( ).split( )))
cards_number = list(map(int, input( ).split( )))

max = 0

for i in range(cards_info[0]):
    for j in range(i + 1, cards_info[0]):
        for k in range(j + 1, cards_info[0]):
            temp = cards_number[i] + cards_number[j] + cards_number[k]
            if temp <= cards_info[1] and temp > max:
                max = temp

print(max)