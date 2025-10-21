import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[]for _ in range(n+1)]
dist = [float('inf')] * (n+1)
cost = 0 

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
s, t = map(int, input().split())

heap = [(0, s)]
dist[s] = 0 

while heap:
    w, cur = heapq.heappop(heap)
    
    if dist[cur] < w:
        continue
    
    for nw, next in graph[cur]:
        cost = w + nw 
        if cost < dist[next]:
            dist[next] = cost 
            heapq.heappush(heap, (cost, next))
            
        
print(dist[t])
        
    