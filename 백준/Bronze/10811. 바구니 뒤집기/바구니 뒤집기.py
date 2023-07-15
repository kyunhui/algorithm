n, m = map(int, input().split())
arr = []
temp = []
for i in range(1,n+1):
    arr.append(i)
for i in range(m):
    a, b = map(int, input().split())
    temp = arr[a-1:b]
    temp.reverse()
    for j in range(b-a+1):
        arr[a-1] = temp[j]
        a += 1
for i in range(len(arr)):
    print(arr[i], end=' ')