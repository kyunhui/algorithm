def solution(diffs, times, limit):
    t = 0 
    length = len(diffs)
    low = 1
    high = max(diffs)

    
    while(low <= high):
        t = 0 
        mid = (low + high) // 2 
        
        for i in range(length):
            if diffs[i] <= mid:
                t += times[i]
            else:
                t += (times[i-1] + times[i]) * (diffs[i] - mid) + times[i]
                
        if t <= limit:
            high = mid - 1
            
        if t > limit: 
            low = mid + 1 
        
    return low