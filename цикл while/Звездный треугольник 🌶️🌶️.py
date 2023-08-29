n = int(input())
for j in range(1, (n+3)//2):
    print('*'*j)
for i in range(n//2, 0, -1):
    print('*'*i)
