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
    
    used = set()
    for i in range(x, n):
        if num[i] in used:
            continue
        used.add(num[i])
        cur.append(num[i])
        dfs(i+1)
        cur.pop()
        
dfs(0)