clock = list(map(int, input().split()))

def get_clock_number(clock):
    min_num = int(''.join(map(str, clock)))
    for i in range(1, 4):
        temp = int(''.join(map(str, clock[i:] + clock[:i])))
        if min_num > temp :
            min_num = temp
    return min_num

clock_num = get_clock_number(clock)

cnt = 1
for i in range(1111, clock_num):
    if '0' not in list(str(i)) and i == get_clock_number(list(map(int, str(i)))):
        cnt += 1
print(cnt)