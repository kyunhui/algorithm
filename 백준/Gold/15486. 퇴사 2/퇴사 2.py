'''
N : 1 <= N <= 1,500,000 이므로 완전탐색으로는 시간초과 -> dp로 풀기 
'''

import sys 

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i + arr[i][0]] + arr[i][1], dp[i+1])

print(dp[0])