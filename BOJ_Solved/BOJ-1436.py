"""
백준 1436번 : 영화감독 숌
"""

count = int(input())

film_number = 666

while(count):
    if '666' in str(film_number):
        count -= 1
        if count != 0:
            film_number += 1
    else:
        film_number += 1

print(film_number)