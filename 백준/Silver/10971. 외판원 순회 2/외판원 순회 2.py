'''
dfs + 백트래킹으로 
'''

import sys 

input = sys.stdin.readline

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n 
cost = 0 
min_cost = float('inf')

def dfs(start, idx, cnt):
    global cost, min_cost
    
    if cnt == n:
        if city[idx][start] != 0:
            min_cost = min(min_cost, cost + city[idx][start])
        return 
    

    for j in range(n):
        if city[idx][j] != 0 and not visited[j]:
            visited[j] = True 
            cost += city[idx][j]
            dfs(start, j, cnt+1)
            cost -= city[idx][j]
            visited[j]= False 
      
visited[0] = True       
dfs(0, 0, 1)

print(min_cost)