# bfs, dfs 문제 
import sys
from collections import deque 
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())


# 딕셔너리 
# graph = {}
# for i in range(1, n+1):
#     graph[i] = set()
    
# for i in range(n-1):
#     a, b = map(int, input().split())
#     graph[a].add(b)
#     graph[b].add(a)
    
# 인접리스트 
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

#dfs 
# def dfs(node):
#     for i in graph[node]:
#         if visited[i] == 0:
#             visited[i] = node
#             dfs(i)
            
# visited[1] = -1            
# dfs(1)

# bfs 
def bfs(x):
    deq = deque([x])
    
    while deq:
        node = deq.popleft()
    
        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = node
                deq.append(adj)
                
bfs(1)
        
for x in range(2, n+1):
    print(visited[x])

