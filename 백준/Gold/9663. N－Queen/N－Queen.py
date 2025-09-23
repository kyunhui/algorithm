n = int(input())
answer = 0

col_used = [False] * n                
diag1_used = [False] * (2*n - 1)      
diag2_used = [False] * (2*n - 1)     

def dfs(row):
    global answer
    if row == n:                      
        answer += 1
        return

    for c in range(n):                
        # 같은 열이나 두 대각선에 이미 퀸이 있으면 불가
        if not col_used[c] and not diag1_used[row + c] and not diag2_used[row - c + n - 1]:
            col_used[c] = True
            diag1_used[row + c] = True
            diag2_used[row - c + n - 1] = True

            dfs(row + 1)             

            col_used[c] = False
            diag1_used[row + c] = False
            diag2_used[row - c + n - 1] = False

dfs(0)
print(answer)