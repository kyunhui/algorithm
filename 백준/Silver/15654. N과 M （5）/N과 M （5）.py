import sys 

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

cur = []
visited = [False] * n 

def dfs(start):
    if len(cur) == m:
        print(*cur)
        return 
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True 
            cur.append(num[i])
            dfs(i+1)
            cur.pop()
            visited[i] = False 

dfs(0)