n = int(input())
a = n // 100
b = n % 100 // 10
c = n % 10
if max(a,b,c) - min(a,b,c) == a+b+c - max(a,b,c) - min(a,b,c):
    print('Число интересное')
else:
    print('Число неинтересное')
