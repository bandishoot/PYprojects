s = input()
l = s.split('.')
flag = 'ДА'
for i in l:
    if 0 <= int(i) <= 255:
        continue
    else:
        flag = 'НЕТ'
print(flag)
