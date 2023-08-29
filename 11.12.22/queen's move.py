a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c or b == d:
    print('YES')
elif a - c == b - d or c - a == b - d:
    print('YES')
else:
    print('NO')
