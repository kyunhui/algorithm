'''
dp! 
index를 뭘로 두는 지 헷갈렸음 
"적어도 c 명을 늘리기위해" 라는 문장을 잘 인지해야 함 
'''

import sys 

input = sys.stdin.readline

c, n = map(int, input().split())
info = []

for _ in range(n):
    a, b = map(int, input().split())
    info.append([a, b])
    
    
dp = [100000] * (c + 100)

dp[0] = 0 

for cost, num in info:
    for i in range(num, c+100):
        dp[i] = min(dp[i-num] + cost, dp[i])
        
print(min(dp[c:]))