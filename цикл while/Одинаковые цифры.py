# put your python code here
n = int(input())
fl = 'YES'
while n >= 10:
    f1 = n % 10
    f2 = n // 10 % 10
    if f1 != f2:
        fl = 'NO'
    n //= 10
print(fl)
