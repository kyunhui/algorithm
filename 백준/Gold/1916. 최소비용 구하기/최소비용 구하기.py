import sys 
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

x, y = map(int, input().split())

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

print(dijkstra(x)[y])

