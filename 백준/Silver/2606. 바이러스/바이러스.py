import sys 
from collections import deque 

input = sys.stdin.readline

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = 1
    
    while que:
        cur = que.popleft()
        for next in graph[cur]:
            if not visited[next]:
                que.append(next)
                visited[next] = 1
                
bfs(1)

print(visited.count(1)-1)