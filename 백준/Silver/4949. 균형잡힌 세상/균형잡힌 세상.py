while(True):
    s = input()
    answer = "yes"
    if s == ".":
        break
    stack = []
    for i in range(len(s)):
        if s[i] == " ":
            continue
        elif s[i] == "(" or s[i] == "[":
            stack.append(s[i])
            continue
        elif s[i] == ")":
            if len(stack) == 0:
                answer = "no" 
                break
            elif stack[-1] == "(":
                stack.pop()
                continue
            else:
                answer = "no" 
                break
        elif s[i] == "]":
            if len(stack) == 0:
                answer = "no"
                break
            elif stack[-1] == "[":
                stack.pop()
                continue
            else :
                answer = "no"
                break    
    if len(stack)==0 and answer == "yes":
        print("yes")
    else:
        print("no")
    
        