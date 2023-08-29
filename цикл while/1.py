n = int(input())
max_digit = 0
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n //= 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)
