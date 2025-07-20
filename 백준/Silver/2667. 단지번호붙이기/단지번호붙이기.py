import sys 
from collections import deque 

input = sys.stdin.readline

n = int(input())

maze = [input() for i in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

def bfs(i, j, cnt):
    que = deque()
    que.append((i, j))
    visited[i][j] = True
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    que.append((nx, ny))
                    cnt += 1
        
    return cnt 


for j in range(n):
    for i in range(n):
        if not visited[i][j] and maze[i][j] == '1':
            answer.append(bfs(i, j, 1))
            
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])