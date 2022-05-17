"""
백준 20499번 : Darius님 한타 안 함?
"""

K, D, A = map(int, input().split('/'))
print('hasu' if K+A < D or D == 0 else 'gosu')