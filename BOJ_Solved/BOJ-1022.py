"""
백준 1022번 : 소용돌이 예쁘게 출력하기
"""

def get_value(x, y):
    idx = max(abs(x), abs(y))
    before_base = (2 * (idx - 1) + 1) ** 2
    base = (2 * idx + 1) ** 2
    dx, dy = idx - x, idx - y

    if x >= y:
        return base - dx - dy
    else:
        return before_base + dx + dy


r1, c1, r2, c2 = map(int, input().split())
graph = []
for i in range(r1, r2 + 1):
    tmp = []
    for j in range(c1, c2 + 1):
        tmp.append(get_value(i, j))
    graph.append(tmp)

max_value = 0
for i in range(len(graph)):
    max_value = max(max_value, *graph[i])

for i in range(len(graph)):
    for j in range(len(graph[i])):
        sub = len(str(max_value)) - len(str(graph[i][j]))
        if sub > 0:
            print(' ' * sub, end='')
        print(graph[i][j], end=' ')
    print('')
