'''
피연산자라면 stack에 append 
연산자라면 stack에서 두 번 pop 해서 계산 후 다시 append 

문제는 입력이 string 

'''

n = int(input())
postfix = input()
number = []
stack = []
values = {}

for i in range(n):
    number.append(int(input()))

for i in range(n):
    values[chr(65 + i)] = number[i]
    

def operate(str, a, b):
    if str == '*':
        return a * b
    elif str == '+':
        return a + b
    elif str == '/':
        return a / b
    else:
        return a - b 
  

for i in range(len(postfix)):
    if postfix[i] == '*' or postfix[i] == '+' or postfix[i] == '/' or postfix[i] == '-':
        a = stack.pop()
        b = stack.pop()
        tmp = operate(postfix[i], b, a)
        stack.append(tmp)
    
    else:
        stack.append(values[postfix[i]])
    
print(f"{stack[0]:.2f}")