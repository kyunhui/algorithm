best = [-1] * 11 
max_diff = -1

def dfs(idx, re, lion, info):
    global best, max_diff 
    if idx == 11:
        l = 0 
        a = 0 
        for i in range(11):
            if lion[i] == 0 and info[i] == 0:
                continue 
            if lion[i] > info[i]:
                l += 10-i 
            else:
                a += 10-i

        diff = l-a

        if diff > max_diff:
            max_diff = diff 
            best = lion.copy()

        elif diff == max_diff and diff > 0: # 동점인 경우 낮은 점수를 많이 맞춘 경우로 
            for i in range(10, -1, -1):
                if lion[i] > best[i]:
                    best = lion.copy()
                    break 
                elif lion[i] < best[i]:
                    break 

        return 

    cur = info[idx] + 1 # 라이언이 이기려면 필요한 화살 수 

    if idx == 10:
        lion[idx] = re 
        dfs(idx+1, 0, lion, info)
        lion[idx] = 0 
        return 
    
    if re >= cur: # 화살을 쏘는 경우 
        lion[idx] = cur 
        dfs(idx+1, re-cur, lion, info)
        lion[idx] = 0 

    dfs(idx+1, re, lion, info) # 안 쏘는 경우

    
def solution(n, info):
    global best, max_diff
    best = [-1] * 11
    lion = [0] * 11
    max_diff = -1
    dfs(0, n, lion, info)
    if max_diff <= 0:
        return [-1]

    return best