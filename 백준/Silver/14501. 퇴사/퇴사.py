import sys 

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0 

# 완전 탐색
def dfs(i, value):
    global answer
    
    if i >= n:
        answer = max(answer, value)
        return
     
    if i + arr[i][0] <= n:
        dfs(i+arr[i][0], value+arr[i][1])
    
    dfs(i+1, value)
    
dfs(0, 0)

print(answer)
