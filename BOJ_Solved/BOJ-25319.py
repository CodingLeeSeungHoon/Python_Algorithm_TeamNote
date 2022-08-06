"""
백준 25319번 : Twitch Plays Vlllbit Explorer
"""

def get_direction(now_x, now_y, x, y):
    ans = ""
    if now_x > x:
        ans += "U"*(now_x-x)
    elif now_x < x:
        ans += "D"*(x-now_x)

    if now_y > y:
        ans += "L"*(now_y-y)
    elif now_y < y:
        ans += "R"*(y-now_y)

    ans += "P"
    maps[x][y] = 0
    return ans


N, M, lenID = map(int, input().split())
maps = [list(input()) for _ in range(N)]
id = input().rstrip()
alpha = [0 for _ in range(26)]

for line in maps:
    for alphabet in line:
        alpha[ord(alphabet)-97] += 1

upgrade = 0
subs = [0 for _ in range(26)]
flag = True

while True:
    for i in id:
        subs[ord(i) - 97] += 1

    for i in id:
        if alpha[ord(i)-97] < subs[ord(i)-97]:
            flag = False
            break

    if not flag:
        break
    upgrade += 1

cnt = 0
now_x, now_y = 0, 0
ans = ""
while cnt != lenID * upgrade:
    for i in range(N):
        for j in range(M):
            if id[cnt % lenID] == maps[i][j]:
                ans += get_direction(now_x, now_y, i, j)
                cnt += 1
                break

ans += get_direction(now_x, now_y, N-1, M-1)
ans = ans[:len(ans)-1]
print(upgrade, len(ans))
print(ans)
