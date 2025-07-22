t = int(input())
temp = 1

answer = []
for _ in range(t):
    n, m = map(int, input().split())
    a = 1
    b = 1
    if(n == m):
        temp = 1
    else:
        i = m
        for _ in range(n):
            a *= i
            i -= 1
        for j in range(1, n + 1):
            b *= j

        temp = a//b
    answer.append(temp)

for i in range(t):
    print(answer[i])