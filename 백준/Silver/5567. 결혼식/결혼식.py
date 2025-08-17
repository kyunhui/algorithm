import sys 
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
    
def bfs(x):
    que = deque()
    que.append(x)
    visited[1] = 1
    
    while que:
        node = que.popleft()
        for next in arr[node]:
            if not visited[next]:
                visited[next] = visited[node] + 1
                que.append(next)
        
bfs(1)

cnt = 0 
for i in range(2, n+1):
    if 2 <= visited[i] <= 3:
        cnt += 1
        
print(cnt)
    
    
    