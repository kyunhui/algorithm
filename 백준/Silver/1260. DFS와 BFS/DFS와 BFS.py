def dfs(v):
    ans_dfs.append(v)
    visited[v] = True
    
    for data in adj[v]:
        if not visited[data]:
            dfs(data)
            
    return ans_dfs
    
def bfs(v):
    q = [v]
    visited[v] = True
    ans_bfs.append(v)
    
    while q:
        tmp = q.pop(0)
        for data in adj[tmp]:
            if not visited[data]:
                q.append(data)
                visited[data] = True
                ans_bfs.append(data)
        
    return ans_bfs

n, m, v = map(int, input().split()) # 노드개수, 엣지개수, 시작노드 
adj = [[] for _ in range(n+1)] 

for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)
    adj[a].append(b)
    
for data in adj:
    data.sort()
    
visited = [False] * (n+1)
ans_dfs = []
print(*dfs(v))

visited = [False] * (n+1)
ans_bfs = []
print(*bfs(v))