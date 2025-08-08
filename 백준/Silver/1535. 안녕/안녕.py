'''
dp 배열을 잘 정의하기 
'''

import sys 

input = sys.stdin.readline

n = int(input())
s = 100 

L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0] * 101

for i in range(n):
    for h in range(100, L[i]-1, -1):
        dp[h] = max(dp[h], dp[h - L[i]] + J[i])
        

print(max(dp[:100]))