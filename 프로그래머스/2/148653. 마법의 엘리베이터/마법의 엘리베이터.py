def solution(storey):
    answer = 0
    
    while storey > 0:
        number = storey % 10
        storey //= 10
        
        if number > 5:
            answer += (10 - number)
            storey += 1
        elif number < 5:
            answer += number
        else:
            if storey % 10 >= 5:
                answer += 5
                storey += 1
            else:
                answer += 5
                
    return answer