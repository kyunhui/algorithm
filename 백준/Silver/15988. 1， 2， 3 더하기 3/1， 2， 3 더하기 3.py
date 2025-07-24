'''
메모리 초과 이슈 -> dp 배열 생성을 효율적이게!! 

'''
import sys 
input = sys.stdin.readline

MOD = 1000000009
dp = [0, 1, 2, 4]

def add(n):
    while len(dp) <= n:
        dp.append((dp[-1] + dp[-2] + dp[-3]) % MOD)
        
    return dp[n]

t = int(input())

for _ in range(t):
    n = int(input())
    
    print(add(n))