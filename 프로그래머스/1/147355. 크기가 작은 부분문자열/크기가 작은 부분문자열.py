def solution(t, p):
    size = len(p)
    cnt = 0 
    
    for i in range(len(t)-size+1):
        tmp = int(t[i:i+size])
        if tmp <= int(p):
            cnt += 1
        
    return cnt