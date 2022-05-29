"""
백준 2941번 : 크로아티아 알파벳
"""

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()
for a in alpha:
    text = text.replace(a, '1')
print(len(text))