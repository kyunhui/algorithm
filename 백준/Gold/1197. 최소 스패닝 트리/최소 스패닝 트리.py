import sys 
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[]for _ in range(V+1)]
visited = [0] * (V+1)
result = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])
    
heap = [[0, 1]]

while heap:
    w, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True 
        result += w  
        
        for next in edge[node]:
            if not visited[next[1]]:
                heapq.heappush(heap, next)
                
print(result)