# 스택을 이용해서 괄호쌍을 찾는다 
# 조합을 이용해서 경우의 수를 찾는다 


from itertools import combinations

def sol(equation):
    n = len(equation)
    stack = []
    pairs = []
    result = set()
    
    # 괄호쌍 체크 
    for i in range(n):
        if equation[i] == '(':
            stack.append(i)
        elif equation[i] == ')':
            start = stack.pop()
            pairs.append((start, i))
    
    # 조합 구하기 
    for i in range(1, len(pairs)+1): # 하나는 제거해야하니까 1 부터 시작 
        for comb in combinations(pairs, i):
            remove_set = set()
            for a, b in comb:
                remove_set.add(a)
                remove_set.add(b)
            new = []
            for i in range(len(equation)):
                if i not in remove_set:
                    new.append(equation[i])
                    
            new_equ = ''.join(new)
            result.add(new_equ)
                
            
    return sorted(result)
    

equation = input()

print(*sol(equation))
