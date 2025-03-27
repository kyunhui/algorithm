def reversing(x):
    x = reversed(list(str(x)))
    x = int((''.join(x)))
    return x 

x, y = map(int, input().split())

x = reversing(x)
y = reversing(y)
answer = reversing(x+y)

print(answer)