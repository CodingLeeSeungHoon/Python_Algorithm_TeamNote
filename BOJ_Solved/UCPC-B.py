import sys
input = sys.stdin.readline

def solution(x1, y1, x2, y2, x3, y3, x4, y4, mx1, mx2, mx3, mx4, my1, my2, my3, my4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            return 1

    return 0


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

if __name__ == '__main__':
    N = int(input())
    baegi = []
    for _ in range(N):
        baegi.append(list(map(int, input().split())))

    baegi.sort(key=lambda x:x[4])
    answer = 0

    for i in range(N):
        x1, y1, x2, y2, weight = baegi[i]
        cnt = 0
        for j in range(i+1, N):
            x3, y3, x4, y4, _ = baegi[j]
            mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
            mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
            if solution(x1, y1, x2, y2, x3, y3, x4, y4, mx1, mx2, mx3, mx4, my1, my2, my3, my4):
                cnt += 1
        answer += (cnt + 1) * weight
    print(answer)