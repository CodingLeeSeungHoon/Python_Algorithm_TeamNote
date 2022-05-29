
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1 * y2) + (x2 * y3) + (x3 * y1) - (y1 * x2) - (y2 * x3) - (y3 * x1)


result = ccw(p1, p2, p3)
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)