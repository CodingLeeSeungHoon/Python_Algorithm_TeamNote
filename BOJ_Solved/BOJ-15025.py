"""
백준 15025번 : Judging Moose
"""
l, r = map(int, input().split())
if l == 0 and r == 0:
    print('Not a moose')
elif l != r:
    print('Odd {}'.format(max(l, r) * 2))
else:
    print('Even {}'.format(r*2))