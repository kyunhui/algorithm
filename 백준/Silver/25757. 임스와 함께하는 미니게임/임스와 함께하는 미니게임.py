a, b = map(str, input().split())
a = int(a)
list = []
cnt = 0

for i in range(a):
    s = input()
    list.append(s)
    
list = set(list)
if b == 'Y':
    print(len(list))
elif b == 'F':
    print(len(list) // 2)
elif b == 'O':
    print(len(list) // 3)