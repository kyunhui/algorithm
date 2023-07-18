n = int(input())
a1 = set(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))


for i in a2:
    if i in a1:
        print(1)
    else:
        print(0)