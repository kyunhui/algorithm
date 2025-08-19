def solution(land):
    n = len(land)
    
    dp = [row[:] for row in land] 
    
    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if k != j)
    
    return max(dp[-1])