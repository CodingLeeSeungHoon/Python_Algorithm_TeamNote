"""
백준 10707번 : 수도요금
"""

x_fee = int(input())
y_fee = int(input())
y_default = int(input())
y_add = int(input())
joi = int(input())

base = joi - y_default if joi - y_default >= 0 else 0

print(min(joi * x_fee, y_fee + base * y_add))