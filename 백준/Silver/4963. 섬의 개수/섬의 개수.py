import sys 
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True 
    
    while que:
        x, y = que.popleft()
        
        for i in range(8):
            nx, ny = dx[i] + x, dy[i] + y
            
            if 0 <= nx < h and 0 <= ny < w:
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True 

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break 
    
    maze = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0 
    
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1 
                
    print(cnt)
                    
    
    
    
    