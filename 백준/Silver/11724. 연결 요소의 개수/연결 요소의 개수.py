import sys 
sys.setrecursionlimit(10**6) 

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v  = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = set()
cnt = 0

def dfs(node, component):
    visited.add(node)
    component.append(node)
    
    for next in graph[node]:
        if next not in visited:
            dfs(next, component)
            
for next in range(1, n+1):
    if next not in visited:
        component = []
        dfs(next, component)
        cnt += 1 
        
print(cnt)
    