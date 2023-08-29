a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < c:
    print('пустое множество')
elif a-c<0 and b - d < 0:
    print(a, b)
elif c == b:
    print(b)
elif a == d:
    print(a)
