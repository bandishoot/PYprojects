s = input()
num = s.split()
number = []
for i in num:
    number.append(int(i))
ind_max = number.index(max(number))
ind_min = number.index(min(number))
number[ind_min], number[ind_max] = ind_max, ind_min
print(number)
