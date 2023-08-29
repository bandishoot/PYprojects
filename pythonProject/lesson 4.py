# quant_countries = input('Vvedite kolichestvo stran: ')
#
# while True:
#     if quant_countries.isnumeric():
#         quant_countries = int(quant_countries)
#         break
#     print('Tolko celye chisla')
#     quant_countries = input('Vvedite kolichestvo stran: ')
#
# dict_countries = dict()
#
# for i in range(quant_countries):
#     country_city = input('vvedite stranu i 3 goroda: ').split()
#     while True:
#         if len(country_city[1:]) >= 3:
#             dict_countries[country_city[0]] = country_city[1:]
#             break
#
#         country_city = input('vvedite stranu i 3 goroda: ').split()
#
# print(dict_countries)

#
#
# quant_countries = input('введите количество стран: ')
#
# while True:
#     if quant_countries.isnumeric():
#         quant_countries = int(quant_countries)
#         break
#
#     print('только целые числа')
#     quant_countries = input('введите количество стран: ')
#
# dict_countries = dict()
# for i in range(quant_countries):
#     country = input(f'введите {i+1}ю страну и 3 города: ').split()
#     while True:
#         if len(country[1:]) >= 3:
#             dict_countries[country[0]] = country[1:]
#             break
#
#         country = input(f'введите {i+1}ю страну и 3 города: ').split()
#
# print(dict_countries)
# print('для выхода из программы введите enter')
#
# while True:
#     city = input('введите город: ')
#
#     if city == '':
#         break
#
#     for key, val in dict_countries.items():
#         if city in val:
#             print(f'{city} находится в стране {key}')
#
#     if flag_not_city:
#         print(f'по городу {city} данных нет')


goods = {
    'Lampa': '12345',
    'Stol': '23456',
    'Divan': '34567',
    'Stul': '45678'
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42}
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ]
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ]
}

dict_res = dict()

for key_1, val_1 in goods.items():
    quant, price, total_price = 0, 0, 0
    for key_2, val_2 in store.items():
        if val_1 == key_2:
            for dict_ in val_2:
                unit = dict_.get('quantity')
                quant += dict_.get('quantity')
                total_unit_price = dict_.get('price') * unit
                total_price += total_unit_price

    dict_res[key_1] = [quant, total_price]

for key, val in dict_res.items():
    print(f'goods {key}, price {val[0]}, quantity {val[1]}')

