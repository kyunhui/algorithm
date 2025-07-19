'''
시작점에서부터 상하좌우로 탐색
짧은 경로 -> 최단경로 문제 

'''

import sys 
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [input()for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0 
visited = [[0 for _ in range(m)] for i in range(n)]

def bfs():
    que = deque()
    que.append((0, 0, 1))
    visited[0][0] = True 
    
    while que:
        x, y, dist = que.popleft()

        if x == n -1 and y == m-1: # 종료조건 
            return dist 
    
        for i in range(4): # 상하좌우 
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    que.append((nx, ny, dist + 1))
                    
print(bfs())