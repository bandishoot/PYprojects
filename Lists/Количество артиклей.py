s = input()
count = 0
for i in s:
    if i.lower() == 'the' or i.lower() == 'a' or i.lower() == 'an':
        count += 1
print(f'Общее количество артиклей: {count}')
