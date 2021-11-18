"""
백준 1181번 : 단어 정렬
"""
num = int(input( ))

word_list = []
for _ in range(num):
    word = input( )
    if word not in word_list:
        word_list.append(word)

word_list = sorted(word_list)
word_list = sorted(word_list, key=lambda x: len(x))

for w in word_list:
    print(w)
