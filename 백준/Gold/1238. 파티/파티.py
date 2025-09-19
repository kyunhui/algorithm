import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    
def dijkstra(start):
    dist = [float('inf')] * (n+1)
    dist[start] = 0 
    heap = [(0, start)]
    
    while heap:
        cur_dist, cur = heapq.heappop(heap)
        if cur_dist > dist[cur]:
            continue
        
        for nxt, w in graph[cur]:
            if dist[nxt] > cur_dist + w:
                dist[nxt] = cur_dist + w
                heapq.heappush(heap, (dist[nxt], nxt))
                
    return dist 

answer = 0 

from_x = dijkstra(x)

for i in range(1, n+1):
    to_x = dijkstra(i)[x]
    total = to_x + from_x[i]
    answer = max(answer, total)

print(answer)