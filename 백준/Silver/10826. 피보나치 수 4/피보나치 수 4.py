from collections import deque

dq = deque()
dq.appendleft(0)
dq.appendleft(1)

num = int(input())

for i in range(num):
    temp = dq[-1]
    dq.pop()
    sum = dq[-1] + temp
    dq.append(temp)
    dq.append(sum)

print(dq[-1])

