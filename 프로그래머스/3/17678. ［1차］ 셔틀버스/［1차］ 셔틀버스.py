def solution(n, t, m, timetable):
    start = 540 # 9 시 
    end = 719 # 11시 59분 
    time = [0] * len(timetable)
    for i in range(len(timetable)):
        h, mi = timetable[i].split(":")
        time[i]=int(h)*60 + int(mi)
    time.sort()
    
    schedule = []
    for i in range(n):
        schedule.append(start + t*i)
    print(schedule)
    
    idx = 0 
    last = 0 
    for bt in schedule:
        cnt = 0 
        while idx < len(time) and time[idx] <= bt and cnt < m:
            last = time[idx]
            cnt += 1
            idx += 1
            
                
    if cnt < m:
        answer = bt
    elif cnt >= m:
        answer = last - 1

    
                
    hh = str(answer // 60).zfill(2)
    mm = str(answer % 60).zfill(2)
    answer = f"{hh}:{mm}"
    return answer