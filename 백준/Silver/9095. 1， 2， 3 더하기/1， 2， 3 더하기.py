import sys
input = sys.stdin.readline

n = int(input())

def dp(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return dp(x-3) + dp(x-2) + dp(x-1)
    
for i in range(n):
    t = int(input())
    print(dp(t))