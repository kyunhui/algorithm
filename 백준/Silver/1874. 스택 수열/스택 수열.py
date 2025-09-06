import sys 

input = sys.stdin.readline

n = int(input())

sequence = []
cnt = 1 
stack = []
answer = []

for _ in range(n):
    a = int(input())
    sequence.append(a)
    
for num in sequence:
    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
        
    if not stack or stack[-1] != num:
        print("NO")
        break 
    
    stack.pop()
    answer.append('-')
    
else:
    print('\n'.join(answer))