'''
bfs로 풀면 되겠다! 
'''

import sys 
from collections import deque 

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
start = int(input())

def bfs(x):
    que = deque()
    visited = [0] * n
    que.append(x)
    visited[x] = True 
    cnt = 1
    
    while que:
        if cnt == n:
            return cnt 
        
        cur = que.popleft()
        move = arr[cur]
        
        if 0 <= cur - move < n:
            cnt += 1 
            que.append(cur-move)
            visited[cur-move] = True 
            
        if 0 <= cur + move < n:
            cnt += 1
            que.append(cur+move)
            visited[cur+move] = True 
                
    return cnt 


print(bfs(start-1))