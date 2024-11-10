import sys
sys.setrecursionlimit(3000)

def lcs(x, y, m, n, memo):
    if m == 0 or n == 0:
        return 0
    
    if memo[m][n] != -1:
        return memo[m][n]
    
    if x[n-1] == y[m-1]:
        memo[m][n] = lcs(x, y, m-1, n-1, memo) + 1
    else:
        memo[m][n] = max(lcs(x, y, m-1, n, memo), lcs(x, y, m, n-1, memo))
        
    return memo[m][n]

x = input()
y = input()
memo = [[-1]*(len(x)+1) for _ in range(len(y)+1)]
print(lcs(x, y, len(y), len(x), memo))