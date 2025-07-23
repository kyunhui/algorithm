import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(n)]
T = int(input())

new_pixel = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0


for i in range(n):
    for j in range(m):
        r, g, b = pixel[i][j*3:(j+1)*3]
        avg = (r + g + b) // 3
        new_pixel[i][j] = 255 if avg >= T else 0

def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True

    while que:
        x, y = que.popleft()
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m:
                if new_pixel[nx][ny] == 255 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))

for i in range(n):
    for j in range(m):
        if new_pixel[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            answer += 1

print(answer)
