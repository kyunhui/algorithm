m = int(input()) 
n = int(input())
check = 0 
array = [] 
 
for i in range(m, n + 1): 
    for j in range(2, i):
        if i % j == 0: 
            check += 1
            break 
    if check == 0 and i != 1:
        array.append(i) 
    check = 0 
    
if len(array) == 0: 
    print(-1) 
else: 
    print(sum(array)) 
    print(min(array)) 
