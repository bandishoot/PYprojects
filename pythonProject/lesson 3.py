# from random import *
#
# lst_range = [randint(37, 45) for _ in range(10)]
# print(lst_range)
#
# quant_of_persons = int(input('vvedite kolvo lydey: '))
#
# print(quant_of_persons)
# lst_range_copy = lst_range[:]
# max_barier_skate = 0
#
# for i in range(quant_of_persons):
#     size = int(input(f'введите размер {i + 1} пары'))
#     if size in lst_range_copy:
#         print(True)
#         lst_range_copy.remove(size)
#         max_barier_skate += 1
#
# print('наибольшее количество людей, которые могут взять коньки: ', max_barier_skate)





str_ = 'husduvchsduvh euhfufhdiwo dhfsfb awdhfdshf wduc'

dict_ = dict()

for i in str_:
    if i in dict_:
        dict_[i] += 1
    else:
        dict_[i] = 1

print(dict_)

