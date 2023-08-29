a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a - c) ** 2 == 1:
    if (b - d) ** 2 == 4:
        print('YES')
    else:
        print('NO')
elif (a - c) ** 2 == 4:
    if (b - d) ** 2 == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
