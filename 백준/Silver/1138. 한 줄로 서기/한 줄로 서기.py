n = int(input())
num = list(map(int, input().split()))

answer = [i for i in range(1, n+1)]
for i in range(n):
    
    if num[i] == 0:
        for j in range(1, n-i):
            a = i + 1
            b = i + j + 1
            if(answer.index(a) > answer.index(b)):
                answer[answer.index(a)], answer[answer.index(b)] = answer[answer.index(b)], answer[answer.index(a)]
    else:
        for j in range(1, num[i]+1): 
            a = i + 1 
            b = i + j + 1 
            a_id = answer.index(a)
            b_id = answer.index(b)
            if answer.index(a) < answer.index(b):
                answer[a_id], answer[b_id] = answer[b_id], answer[a_id]

for i in answer:
    print(i, end=" ")