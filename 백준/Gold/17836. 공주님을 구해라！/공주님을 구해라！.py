'''
gram 여부에 따른 visited 배열 상태 관리.. 가 중요! 
'''

import sys 
from collections import deque 

input = sys.stdin.readline
n, m, t = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(n)]

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    que = deque() 
    que.append((0, 0, 0, 0)) # x, y, t, gram 여부 
    visited[0][0][0] = True 
    
    while que:
        x, y, cnt, gram = que.popleft()
        
        if cnt > t:
            break 
        
        if x == n-1 and y == m-1:
            return cnt
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1: # 벽일 때 
                    if gram == 1 and not visited[nx][ny][1]: # gram을 가지고 있으면 
                        visited[nx][ny][1] = True 
                        que.append((nx, ny, cnt + 1, 1))
                        
                    
                elif maze[nx][ny] == 0: # 벽이 아닐 때 
                    if not visited[nx][ny][gram]: # 그냥 통과 가능 
                        visited[nx][ny][gram] = True 
                        que.append((nx, ny, cnt+1, gram))
                        
                else: # gram일 때 
                    if not visited[nx][ny][1]: # 그냥 통과 
                        visited[nx][ny][1] = True 
                        que.append((nx, ny, cnt+1, 1))
                
    return -1
                    
answer = bfs()

if answer == -1:
    print('Fail')
else:
    print(answer)