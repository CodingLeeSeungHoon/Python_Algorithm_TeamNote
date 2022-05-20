"""
백준 21633번 : Bank Transfer
"""

k = int(input())

fee = 25 + k * 0.01
fee = 2000 if fee > 2000 else fee
print(fee)