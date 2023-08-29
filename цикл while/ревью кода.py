# put your python code here
n = int(input())
quantity, last_digit, chet_quantity, summa, mult, quan, l_digit = 0, n % 10, 0, 0, 1, 0, 0
while n > 0:
    if n % 10 == 3:
        quantity += 1
    if n % 10 > 5:
        summa += 1
    if n % 10 == 0 or n % 10 == 5:
        quan += 1
    if n % 10 > 7:
        mult *= n
    if n % 2 == 2:
        chet_quantity += 1
    n //= 10
    if last_digit == n % 10:
        l_digit += 1
print(quantity, last_digit, chet_quantity, summa, mult, quan, sep='\n')
