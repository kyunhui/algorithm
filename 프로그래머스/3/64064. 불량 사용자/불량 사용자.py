'''
백트래킹 같은데, 일단 가능한 경우의 수를 체크하고 거기서 조합? 
'''
            
def solution(user_id, banned_id):
    n = len(user_id)
    m = len(banned_id)
    print(n, m)
    cur = []
    result = set()
    
    def match(user, ban):
        if len(user) != len(ban):
            return False
        for uc, bc in zip(user, ban):
            if bc != '*' and uc != bc:
                return False 
        return True 

    def dfs(idx):  
        nonlocal n, m
        
        if idx == m:
            result.add(tuple(sorted(cur)))
            return 
        
        for j in range(n):
            if match(user_id[j], banned_id[idx]):
                if user_id[j] not in cur:
                    cur.append(user_id[j])
                    dfs(idx+1)
                    cur.pop()
    dfs(0)    
    return len(result)