import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(n)]
T = int(input())

new_pixel = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        r = pixel[i][j*3]
        g = pixel[i][j*3+1]
        b = pixel[i][j*3+2]
        avg = (r + g + b) // 3
        if avg >= T:
            new_pixel[i][j] = 255
        else:
            new_pixel[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if new_pixel[nx][ny] == 255 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

answer = 0
for i in range(n):
    for j in range(m):
        if new_pixel[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            answer += 1

print(answer)