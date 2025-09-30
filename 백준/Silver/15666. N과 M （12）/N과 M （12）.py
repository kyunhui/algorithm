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
    
    prev = 0 
    for i in range(x, len(num)):
        if prev == num[i]:
            continue
        cur.append(num[i])
        dfs(i)
        cur.pop()
        prev = num[i]
dfs(0)     
        