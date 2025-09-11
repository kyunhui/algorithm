def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    max_cnt, max_total = 0, 0
    n = len(users)
    m = len(emoticons)
    
    def dfs(idx, discounts):
        nonlocal max_cnt, max_total 
        
        if idx == m:
            cnt, total = 0, 0
            
            for r, limit in users:
                tmp = 0 
                for i in range(m):
                    emot = emoticons[i]
                    disc = discounts[i]
                    if disc >= r: # 원하는 할인율 이상이면 
                        tmp += emot - emot * (disc/100)
                        
                if tmp >= limit:
                    cnt += 1
                else:
                    total += tmp 
                    
            if cnt > max_cnt:
                max_cnt = cnt
                max_total = total 
                
            elif cnt == max_cnt and total > max_total:
                max_total = total 
            
            return 
                
        for e in sale:
            dfs(idx+1, discounts+[e])
            
    dfs(0, [])
    
    return [max_cnt, int(max_total)]