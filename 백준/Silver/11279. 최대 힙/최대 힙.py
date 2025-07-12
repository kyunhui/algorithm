import sys, heapq

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    
    if num == 0:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap) * (-1))
        
    else:
        heapq.heappush(heap, -num)
        