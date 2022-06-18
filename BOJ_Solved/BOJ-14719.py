"""
백준 14719번 : 빗물
"""

def check_right(a, b):
    while b < w:
        if ground[a][b] == 1 or ground[a][b] == 2:
            break
        b += 1
    return b

def check_left(c, d):
    while d >= 0:
        if ground[c][d] == 1 or ground[c][d] == 2:
            break
        d -= 1
    return d


h, w = map(int, input().split())
ground = [[0 for _ in range(w)] for _ in range(h)]
wall_list = list(map(int, input().split()))

for idx, wall in enumerate(wall_list):
    for i in range(1, wall+1):
        ground[-i][idx] = 1


for i in range(h-1, -1, -1):
    for j in range(w-1, -1, -1):
        if ground[i][j] == 1:
            continue
        if ground[i][j] == 0:
            right = check_right(i, j)
            left = check_left(i, j)

            if right != w and left != -1:
                ground[i][j] = 2

ans = 0
for g in ground:
    ans += g.count(2)

print(ans)