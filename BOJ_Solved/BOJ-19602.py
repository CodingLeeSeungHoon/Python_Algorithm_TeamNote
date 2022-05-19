"""
백준 19602번 : Dog Treats
"""
s = int(input())
m = int(input())
l = int(input())
print('happy' if s + 2*m + 3*l >= 10 else 'sad')