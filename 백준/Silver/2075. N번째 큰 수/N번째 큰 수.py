import sys, heapq

input = sys.stdin.readline
n = int(input())

heap = []

for i in range(n):
    arr = list(map(int, input().split()))
    if not heap:
        for item in arr:
            heapq.heappush(heap, item)
    else:
        for item in arr:
            if heap[0] < item:
                heapq.heappush(heap, item)
                heapq.heappop(heap)
                
    
print(heap[0])