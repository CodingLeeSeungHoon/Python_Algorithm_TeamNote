"""
백준 14065번 : Gorivo
"""

mile = float(input())
kilometer = mile * 1.609344  # n 킬로미터 -> 3.785411784 리터
print((3.785411784 / kilometer) * 100)