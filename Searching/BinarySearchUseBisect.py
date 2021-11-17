from bisect import bisect_left, bisect_right
import bisect

def index(a, x):
    # 리스트 내의 원소의 위치 반환, 없으면 에러
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    # x 보다는 작은 최대 값 반환
    i = bisect_left(a, x) # left는 x가 a에 이미 있다면 기존 항목 앞에 위치하기 때문에
    if i:
        return a[i-1] # i-1 이면 x 보다는 작은 최대값이다.
    raise ValueError

def find_le(a, x):
    # x 보다 작거나 같은 최대 값 반환
    i = bisect_right(a, x) # right는 x가 a에 이미 있다면 기존 항목 한 칸 뒤에 위치하기 때문에
    if i:
        return a[i-1] # i-1 이면 x 보다 작은 최대값 혹은 동일 값이다.
    raise ValueError

def find_gt(a, x):
    # x 보다는 큰 최소 값 반환
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    # x 보다는 크거나 같은 최소 값 반환
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


# [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]
