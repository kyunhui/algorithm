import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

s = int(input())

graph = [[] for _ in range(v+1)]
dist = [float('inf')] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

    
    
heap = [(0, s)]
dist[s] = 0  
cost = 0 

while heap:
    w, cur = heapq.heappop(heap)
    
    if dist[cur] < w:
        continue
    
    for nw, next in graph[cur]:
        cost = w + nw 
        if dist[next] > cost:
            dist[next] = cost
            heapq.heappush(heap, (cost, next))
            
for d in dist[1:]:
    print(d if d != float('inf') else 'INF')