'''
MST 
prim : 시간초과...
-> 방문했으면 continue 해보기 
 
'''
import sys 
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)
cost = 0 
result = 0 

for _ in range(e):
    a, b, c = map(int, input().split())
    cost += c 
    graph[a].append([c, b])
    graph[b].append([c, a])

     
heap = [[0, 1]]

while heap:
    c, node = heapq.heappop(heap)
    if visited[node]:
        continue
    result += c 
    visited[node] = True 
        
    for next in graph[node]:
        if not visited[next[1]]:
            heapq.heappush(heap, next)

if not all(visited[1:]):
    print(-1)
else:
    print(cost - result) 