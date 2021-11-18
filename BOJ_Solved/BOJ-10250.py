"""
백준 10250번 : ACM 호텔
"""
test = int(input( ))

for _ in range(test):
    H, W, N = map(int, input( ).split( ))

    rest = N % H  # 4
    value = N // H  # 1
    if rest == 0:
        rest = H
        value -= 1

    if value + 1 < 10:
        value = '0' + str(value + 1)
    else:
        value = str(value + 1)

    print("{}{}".format(rest, value))
