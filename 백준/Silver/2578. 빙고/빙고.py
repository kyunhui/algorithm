import sys 

input = sys.stdin.readline

bingo = [list(map(int, input().split()))for _ in range(5)]
arr = [list(map(int, input().split()))for _ in range(5)]
check = [[0 for _ in range(5)]for _ in range(5)]

cnt = 0 

def idx(x):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == x:
                return i, j
def checking(check):
    cnt = 0 
    
    # 가로 
    for x in check:
        if x.count(1) == 5:
            cnt += 1
            
    # 세로 
    for i in range(5):
        y = 0 
        for j in range(5):
            if check[j][i] == 1:
                y += 1
                
        if y == 5:
            cnt += 1
            
    # 왼쪽 위 대각선 
    d1 = 0 
    for i in range(5):
        if check[i][i] == 1:
            d1 += 1
            
    if d1 == 5:
        cnt += 1
        
    # 오른쪽 위 대각선 
    d2 = 0 
    for i in range(5):
        if check[i][4-i] == 1:
            d2 += 1
            
    if d2 == 5:
        cnt += 1 
    
    return cnt 

margin = 0 

for i in range(5):
    for j in range(5):
        tmp = arr[i][j]
        a, b = idx(tmp)
        check[a][b] = 1 
        margin += 1 
        
        if margin >= 12:
            if checking(check) >= 3:
                print(margin)
                sys.exit(0)
    