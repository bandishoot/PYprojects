a = int(input())
if a > 36 or a < 0:
    print('ошибка ввода')
if a == 0:
    print('зеленый')
if 1 <= a <= 10 and a % 2 == 0:
    print('черный')
elif 1 <= a <= 10 and a % 2 != 0:
    print('красный')
if 10 < a <= 18 and a % 2 == 0:
    print('красный')
elif 10 < a <= 18 and a % 2 != 0:
    print('черный')
if 18 < a <= 28 and a % 2 == 0:
    print('черный')
elif 18 < a <= 28 and a % 2 != 0:
    print('красный')
if 28 < a <= 36 and a % 2 == 0:
    print('красный')
elif 28 < a <= 36 and a % 2 != 0:
    print('черный')
