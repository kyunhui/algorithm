n = int(input())
time = []

for _ in range(n):
    a, b = map(int, input().split())
    time.append([a, b])

time.sort(key=lambda a : a[0])
time.sort(key=lambda a : a[1])

last = 0 
count = 0 

for a, b in time:
    if a >= last:
        count += 1
        last = b
        
print(count)