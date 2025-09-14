import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
cur = []

def dfs(x):
    
    if len(cur) == m:
        print(*cur)
        return 
    
    for i in range(x, n):
        cur.append(num[i])
        dfs(i)
        cur.pop()
        
dfs(0)
        