a = input()
b = input()
k = 'красный'
s = 'синий'
j = 'желтый'
if (a != k and a != s and a != j) or (b != k and b != s and b != j):
    print('ошибка цвета')
else:
    if a == k and b == k:
        print('красный')
    elif a == k and b == s or a == s and b == k:
        print('фиолетовый')
    elif a == s and b == s:
        print(s)
    elif a == s and b == j or a == j and b == s:
        print('зеленый')
    elif a == j and b == j:
        print(j)
    elif a == j and b == k or a == k and b == j:
        print('оранжевый')
