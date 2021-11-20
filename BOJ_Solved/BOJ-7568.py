"""
백준 7568번 : 덩치
"""

num = int(input( ))
w = []
h = []

rank = []

for _ in range(num):
    person_info = list(map(int, input( ).split( )))
    w.append(person_info[0])
    h.append(person_info[1])
    rank.append(1)

for i in range(num):
    for j in range(i + 1, num):
        if w[i] > w[j] and h[i] > h[j]:
            rank[j] += 1
        elif w[i] < w[j] and h[i] < h[j]:
            rank[i] += 1

for index in range(num):
    print(rank[index])