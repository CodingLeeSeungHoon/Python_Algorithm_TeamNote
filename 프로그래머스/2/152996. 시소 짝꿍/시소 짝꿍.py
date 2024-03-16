from collections import defaultdict

def solution(weights):
    answer = 0
    history = defaultdict(int)
    
    for w in weights:
        answer += history[w] + history[w*2] + history[w/2] + history[(2*w)/3] + history[(3*w)/2] + history[(3*w)/4] + history[(4*w)/3]
        history[w] += 1
        
    return answer