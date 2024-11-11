x = int(input())
memo = [1e9] * 1000010

memo[1] = 0
for i in range(1, x+1):
    if i*3 <= x:
        memo[i*3] = min(memo[i*3], memo[i]+1)
    if i*2 <= x:
        memo[i*2] = min(memo[i*2], memo[i] + 1)
    memo[i+1] = min(memo[i+1], memo[i] + 1)

print(memo[x])