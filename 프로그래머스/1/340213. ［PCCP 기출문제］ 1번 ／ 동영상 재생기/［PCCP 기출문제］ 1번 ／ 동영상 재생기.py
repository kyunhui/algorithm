def change(s):
    s = s.replace(':', '')
    s = (int(s[0]) * 10 + int(s[1])) * 60 + int(s[2]) * 10 + int(s[3])
    return s 

def solution(video_len, pos, op_start, op_end, commands):
    video_len = change(video_len)
    pos = change(pos)
    op_start = change(op_start)
    op_end = change(op_end)
    
    for i in range(len(commands)):
        if op_start <= pos <= op_end:
            pos = op_end
            
        if commands[i] == "next":
            pos += 10 
            if pos > video_len:
                pos = video_len
            if pos == op_end:
                continue
            
        if commands[i] == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
            if pos == op_start:
                continue
                
    if op_start <= pos <= op_end:
            pos = op_end
    
    m = pos // 60
    s = pos % 60
    answer = '' 
    
    if m // 10 == 0:
        m = '0' + str(m)
        
    if s // 10 == 0:
        s = '0' + str(s)
        
    answer = str(m) + ':' +  str(s)
    print(answer)
    return answer

