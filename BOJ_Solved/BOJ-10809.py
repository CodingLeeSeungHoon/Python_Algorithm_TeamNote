"""
백준 10809번 : 알파벳 찾기
"""
alpha = {}

for alphabet in 'abcdefghijklmnopqrstuvwxyz':
    alpha[alphabet] = -1

word = input( )

for index, w in enumerate(word):
    if alpha[w] == -1:
        alpha[w] = index

for a in alpha:
    print(alpha[a], end=' ')
