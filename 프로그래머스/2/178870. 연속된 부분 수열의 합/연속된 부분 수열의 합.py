def solution(sequence, k):
    answer = []
    
    length = len(sequence)
    start, end = 0, 0
    total = 0
    candidate = int(1e10)
    
    while start <= end:
        while total < k and end < length:
            total += sequence[end]
            end += 1
        if total == k and end - start < candidate:
            answer = [start, end - 1]
            candidate = end - start
        
        if start != end:
            total -= sequence[start]
        start += 1
        

    # if total == k and end - start < candidate:
    #     answer = [start, end - 1]
    #     candidate = end - start
        
    return answer