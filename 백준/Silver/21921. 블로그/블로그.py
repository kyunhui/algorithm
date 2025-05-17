def blog(n, x, visitor):
    window = sum(visitor[:x])
    answer = window
    cnt = 1 
    
    for i in range(x, n):
        # 윈도우 를 한 칸씩 옮기기 
        window = window - visitor[i-x] + visitor[i]
        if window > answer:
            answer = window
            cnt = 1
            
        elif window == answer:
            cnt += 1
            
    if answer == 0:
        return ('SAD', )
    else:
        return (answer, cnt)

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

print(*blog(n, x, visitor))
