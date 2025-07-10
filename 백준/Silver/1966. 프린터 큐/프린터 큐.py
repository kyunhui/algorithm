from queue import deque

def printer(n, m, value):
    q = deque()
    for i in range(n):
        q.append((i, value[i]))  # (문서 번호, 중요도)

    count = 0

    while q:
        idx, priority = q.popleft()
        
        found_higher = False
        for _, other_priority in q:
            if priority < other_priority:
                found_higher = True
                break

        if found_higher:
            q.append((idx, priority))
        else:
            count += 1 
            if idx == m:
                return count
       

t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    value = list(map(int, input().split()))
    print(printer(n, m, value))
    
        
        