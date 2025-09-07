'''
dist 배열 쓰기 !!! 
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    dist = [-1] * (n+1)   
    dist[start] = 0
    
    que = deque([start])
    
    while que:
        now = que.popleft()
        
        for nxt in graph[now]:
            if dist[nxt] == -1:   
                dist[nxt] = dist[now] + 1
                que.append(nxt)
    
    result = [i for i in range(1, n+1) if dist[i] == k]
    return result

answer = bfs(x)

if not answer:
    print(-1)
else:
    answer.sort()
    print(*answer, sep="\n")