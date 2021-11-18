"""
백준 15829번 : Hashing
"""

n = int(input())
numbers = input()

cnt = 0
sum_num = 0

for n in numbers:
    new_num = ord(n) - 96
    mul = 31 ** cnt

    sum_num += new_num * mul
    cnt += 1

print(sum_num % 1234567891)