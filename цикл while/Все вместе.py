n = int(input())
x = n
summa = 0
quan = 0
mult = 1
aver = 0
f1 = n // (10 ** len(str(n//10)))
while n > 0:
    summa = summa + n % 10
    quan += 1
    mult *= n % 10
    aver = summa / quan
    n //= 10
print(summa, quan, mult, aver, f1, f1 + (x % 10), sep='\n')
