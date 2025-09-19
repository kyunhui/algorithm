from collections import deque 

def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cost = [[[float('inf')]*4 for _ in range(n)]for _ in range(n)]
    que = deque()
    
    for i in range(4):
        cost[0][0][i] = 0 
        que.append((0, 0, i, 0))

    while que:
        x, y, d, cur = que.popleft()
        
        for nd in range(4):
            nx, ny = x + dx[nd], y + dy[nd]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if nd == d: # 이러면 직선이 맞나 
                    new_cost = cur + 100
                else:
                    new_cost = cur + 600
                    
                if new_cost < cost[nx][ny][nd]:
                    cost[nx][ny][nd] = new_cost
                    que.append((nx, ny, nd, new_cost))                    
                
    
    return min(cost[n-1][n-1])