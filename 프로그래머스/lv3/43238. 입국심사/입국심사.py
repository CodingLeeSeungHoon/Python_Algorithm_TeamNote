def check(n, times, k):
    can_enter = 0
    for t in times:
        can_enter += k // t
    return True if can_enter >= n else False

def solution(n, times):
    answer = 0
    start = min(times)
    end = min(times) * n
    mid = start
    
    while mid + 1 != end:
        mid = (start + end) // 2
        if check(n, times, mid):
            end = mid
        else:
            start = mid
        
    return end