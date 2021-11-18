"""
백준 2675번 : 문자열 반복
"""

test = int(input( ))

for _ in range(test):
    num, word = input( ).split( )
    num = int(num)
    string = ''

    for w in word:
        string += w * num
    print(string)