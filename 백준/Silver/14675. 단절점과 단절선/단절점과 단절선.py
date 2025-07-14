'''
트리는 사이클이 없어서 모든 선이 단절선 
degree >= 2 라면 단절점 
'''

import sys 

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
q = int(input()) # query 개수 

for i in range(1, q+1):
    t, k = map(int, input().split())
    if t == 1:
        if len(graph[k]) >= 2:
            print('yes')
        else:
            print('no')
        continue
        
    if t == 2:
        print('yes')

    