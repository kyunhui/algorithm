def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        tmp = ord(my_string[i])
        if 48 <= tmp <= 57:
            answer.append(tmp-48)
    answer.sort()
    return answer 