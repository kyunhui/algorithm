import copy 

def solution(emergency):
    answer = []
    
    arr = copy.deepcopy(emergency)
    arr.sort(reverse=True)
    for i in range(1, len(arr)+1):
        answer.append(arr.index(emergency[i-1])+1)
    
    return answer