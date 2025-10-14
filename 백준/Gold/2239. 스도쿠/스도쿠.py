import sys 

input = sys.stdin.readline

def row_check(row, num):
    for col in range(9):
        if sdoku[row][col] == num:
            return False
    return True 

def col_check(col, num):
    for row in range(9):
        if sdoku[row][col] == num:
            return False
    return True 

def box_check(row, col, num):
    row = (row // 3) * 3 # 0, 3, 6 중 하나 
    col = (col // 3) * 3 
    
    for i in range(3):
        for j in range(3):
            if sdoku[row+i][col+j] == num:
                return False 
            
    return True 
    
    
def dfs(depth):
    if depth == len(blank):
        for i in range(9):
            print(''.join(map(str, sdoku[i])))
        sys.exit(0)
    
    nr, nc = blank[depth]
    
    for i in range(1, 10):
        if row_check(nr, i) and col_check(nc, i) and box_check(nr, nc, i):
            sdoku[nr][nc] = i
            dfs(depth+1)
            sdoku[nr][nc] = 0 
    
    
sdoku = []
blank = []

for i in range(9):
    tmp = list(map(int, input().rstrip()))
    for j in range(len(tmp)):
        if tmp[j] == 0:
            blank.append((i, j))
    sdoku.append(tmp)
    
dfs(0)

