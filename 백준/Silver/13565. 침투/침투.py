import sys 
from collections import deque

input = sys.stdin.readline

n, m  = map(int, input().split())
maze = [input() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()

def bfs():
    answer = 'NO'
    
    while que:
        x, y = que.popleft()
        
        if x == n-1 and maze[x][y] == '0': # 침투성공
            answer = 'YES' 
            return answer 
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '0' and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True 

    return answer 

for i in range(m):
    if maze[0][i] == '0':
        que.append((0, i))
        visited[0][i] = True 
        
print(bfs())

