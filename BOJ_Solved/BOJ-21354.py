"""
백준 21354번 : Äpplen och päron
"""

a, b = map(int, input().split())
print('lika' if 7*a == 13*b else 'Axel' if 7*a > 13*b else 'Petra')