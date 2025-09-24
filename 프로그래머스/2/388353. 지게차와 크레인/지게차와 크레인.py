from collections import deque 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    storage = [list(s) for s in storage]
    
    def bfs():
        visited = [[False] * m for _ in range(n)]
        que = deque()
        
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and storage[i][j] == '.':
                    visited[i][j] = True 
                    que.append((i, j))
        
        while que:
            x, y = que.popleft()
            
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if storage[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True 
                        que.append((nx, ny))
                        
        return visited
    
    for re in requests:
        if len(re) == 1: # 지게차 
            visited = bfs()
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == re:
                        flag = False 
                        
                        if i == 0 or i == n-1 or j == 0 or j == m-1:
                            flag = True
                        else:
                            for d in range(4):
                                nx, ny = dx[d] + i, dy[d] + j
                                if 0 <= nx < n and 0 <= ny < m:
                                    if visited[nx][ny]:
                                        flag = True 
                                        break 
                        if flag:
                            storage[i][j] = '.'
        else: # 크레인 
            cur = re[0]
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == cur:
                        storage[i][j] = '.'
    answer = 0 
    
    for i in range(n):
        for j in range(m):
            if storage[i][j] != '.':
                answer += 1
                
                
    return answer