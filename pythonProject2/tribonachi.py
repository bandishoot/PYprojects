str_ = input().split()
for i in str_:
    i.strip('0')
print(str_)
for i in range(len(str_)):
    if str_[i] == str_[i+1]:
        print('YES')
    else:
        print('NO')

