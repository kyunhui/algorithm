def solution(n, candy, answer):           
    for i in range(n):
        for j in range(n):
            # 오른쪽과 교환 
            if j+1 < n and candy[i][j] != candy[i][j+1]:
                candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
                answer = max(answer, check())
                candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
                
            # 아래쪽과 교환
            if i + 1 < n and candy[i][j] != candy[i+1][j]:
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
                answer = max(answer, check())
                
                candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
                
    return answer

def check():
    # 세로 검사 
    maxcnt = 1 
    
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if candy[i-1][j] == candy[i][j]:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
            else:
                cnt = 1
             
    # 가로 검사 
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candy[i][j-1] == candy[i][j]:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
            else:
                cnt = 1
                
                


    return maxcnt

n = int(input())

candy = [list(input()) for _ in range(n)]
answer = 0
print(solution(n, candy, answer))


