'''

시간초과 
각 열에 대해 bfs()를 계속 호출하면 visited 배열을 새로 초기화, 탐색 초기화 이슈 ->  O(n x m^2)
모든 '0'의 위치를 먼저 큐에 넣고 bfs()를 한 번 호출 -> O(n x m)

'''

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
    while que:
        x, y = que.popleft()
        
        if x == n-1: # 마지막 행이면 성공
            return 'YES'
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '0' and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True 

    return 'NO'

for i in range(m):
    if maze[0][i] == '0':
        que.append((0, i))
        visited[0][i] = True 
        
print(bfs())

