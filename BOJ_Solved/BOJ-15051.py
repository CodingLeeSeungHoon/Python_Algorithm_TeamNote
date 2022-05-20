"""
백준 15051번 : Máquina de café
"""

a = int(input())
b = int(input())
c = int(input())

print(min(4*a+2*b, 2*a+2*c, 2*b+4*c))