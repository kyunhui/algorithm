import sys 
from collections import deque 

input = sys.stdin.readline
n = int(input())

deq = deque(enumerate(map(int, input().split())))
answer = []

while deq:
    idx, curr = deq.popleft()
    answer.append(idx + 1)
    
    if curr > 0:
        deq.rotate(-(curr - 1))
        
    elif curr < 0:
        deq.rotate(-curr)
        
print(' '.join(map(str, answer)))    
    