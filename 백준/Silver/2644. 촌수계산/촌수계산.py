import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 연결

visited = [False] * (n+1)
answer = -1

def dfs(cur, depth):
    global answer
    if cur == b:         
        answer = depth
        return
    visited[cur] = True
    for nx in graph[cur]:
        if not visited[nx]:
            dfs(nx, depth + 1)

dfs(a, 0)
print(answer)