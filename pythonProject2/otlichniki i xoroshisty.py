# put your python code here
quantity = int(input())
lst_ = [input().split() for i in range(quantity)]
lst_otl = []
for i in lst_:
    for j in i:
        print(j, end=' ')
    print()
print()
# вывод списка в начальном порядке

for j in lst_:
    if int(j[1]) >= 4:
        lst_otl.append(j)
# список хорошистов и отличников

# for i in range(len(lst_otl)):
#     for j in range(i+1, len(lst_otl)):
#         if int(lst_otl[i][1]) > int(lst_otl[j][1]):
#             lst_otl[i][1], lst_otl[j][1] = lst_otl[j][1], lst_otl[i][1]
# сортировка

for i in lst_otl:
    for j in i:
        print(j, end=' ')
    print()




