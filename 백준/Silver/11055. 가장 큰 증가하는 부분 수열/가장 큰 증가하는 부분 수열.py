import sys 

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [1 for _ in range(n+1)]
dp[0] = num[0]

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])
        else:
            dp[i] = max(dp[i], num[i])
            
            
print(max(dp))