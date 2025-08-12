import sys 

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for j in range(1, m+1):
        dp[1][j] = j
        
    for i in range(2, n+1):
        for j in range(1, m+1):
            if 2 ** (i-1) > j:
                dp[i][j] = 0 
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
        
    print(dp[n][m])