import sys
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())

photo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0 
max_area = 0 

def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = True 
    cnt = 1
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if photo[nx][ny] == 1 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1 

    return cnt 

for i in range(n):
    for j in range(m):
        if photo[i][j] == 1 and not visited[i][j]:
            count += 1
            area = bfs(i, j)
            if area > max_area:
                max_area = area
                
print(count)
print(max_area)
            
            