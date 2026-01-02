import sys 

input = sys.stdin.readline

n = int(input())
ans = 0 

for _ in range(n):
    stack = []
    word = input().rstrip()
    
    for w in word:
        if not len(stack):
            stack.append(w)
        elif stack[-1] == w:
            stack.pop(-1)
        else:
            stack.append(w)
    if not len(stack):
        ans += 1
        
print(ans)