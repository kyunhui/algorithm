def solution(n, q, ans):
    answer = 0
    cur = []
    
    def dfs(start):
        nonlocal answer 
        
        if len(cur) == 5:
            for i in range(len(q)):
                case = q[i]
                answ = ans[i]
                if len(set(cur) & set(case)) != answ:
                    return 
            answer += 1 
            return 
        
        for i in range(start, n+1):
            cur.append(i)
            dfs(i+1)
            cur.pop()
            
    dfs(1)
            
    return answer

