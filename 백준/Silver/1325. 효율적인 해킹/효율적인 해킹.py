import sys 
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

value = []

def bfs(x):
    que = deque([x])
    cnt = 1
    visited = [0] * (n+1)
    visited[x] = True
    
    while(que):
        a = que.popleft()
        for node in graph[a]:
            if not visited[node]:
                visited[node] = True 
                que.append(node)
                cnt += 1
            
    return cnt 
        
for i in range(1, n+1):
    tmp = bfs(i)
    value.append(tmp)

answer = max(value)

for i in range(n):
    if answer == value[i]:
        print(i+1, end= ' ')

    