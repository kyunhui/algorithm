n, k = map(int, input().split())

arr = []
answer = []

for i in range(1, n+1):
    arr.append(i)
    
idx = 0

while len(arr) != 0:
    idx += (k-1)
    idx = idx % len(arr)
    answer.append(arr.pop(idx))


print('<', end='')
for i in range(n-1):
    print(answer[i], end=", ")
print(answer[n-1], end="")
print(">", end="")