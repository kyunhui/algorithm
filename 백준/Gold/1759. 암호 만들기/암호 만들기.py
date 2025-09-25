import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = input().split()
s.sort()
ans = []
vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(x, depth):
    if depth == n:
        vcnt = 0 
        for ch in ans:
            if ch in vowels:
                vcnt+= 1
        ccnt = n - vcnt
        
        if vcnt >= 1 and ccnt >= 2:
            print("".join(ans))
            
        return 
    
    for i in range(x, m):
        ans.append(s[i])
        dfs(i+1, depth+1)
        ans.pop()
        
dfs(0, 0)
