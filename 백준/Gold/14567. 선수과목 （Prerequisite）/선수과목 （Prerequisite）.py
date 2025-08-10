'''
위상정렬? -> 선행조건을 지키면서 나열 
indegree를 사용해서 진입차수가 0(우선순위)인 node 를 que에 넣어서 먼저 처리하기 
다음 순서는 -1 하여 indegree가 0 이면 que에 추가하여 처리 
'''

import sys
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())
sub = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
answer = [1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    sub[a].append(b)
    indegree[b] += 1
    
que = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)
        
while que:
    node = que.popleft()
    
    for next in sub[node]:
        indegree[next] -= 1
        answer[next] = max(answer[node]+1, answer[next])
        if indegree[next] == 0:
            que.append(next)
                        
print(*answer[1:])
        
        