def solution(x, y, n):
    answer = 0
    dp = [-1 for _ in range(y+1)]
    dp[x] = 0
    
    for i in range(x, y+1):
        candidate = []
        if i >= x + n and dp[i - n] != -1:
            candidate.append(dp[i - n])
        if i % 2 == 0 and dp[i // 2] != -1:
            candidate.append(dp[i // 2])
        if i % 3 == 0 and dp[i // 3] != -1:
            candidate.append(dp[i // 3])
        
        if candidate:
            dp[i] = min(candidate) + 1
        
    return dp[y]