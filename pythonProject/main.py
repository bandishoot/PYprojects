shop = [
    ['karetka', 1200],
    ['shatun', '1000r'],
    ['pedal', 300],
    ['RAMA', '12000rub'],
    ['Obod', 2000],
    ['shatun', 200],
    ['sedlo', 2700]
]

alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
lst = []

detail = input()
s = 0
quantity = 0
for i in shop:
    if i[0].lower() == detail.lower():
        if type(i[1]) is int:
            s += i[1]
            quantity += 1
        else:
            for j in range(len(i[1])):
                if i[1][j] not in alphabet:
                    lst.append(i[1][j])
            new_lst = ''.join(lst)
            s += int(new_lst)
            quantity += 1
print(quantity, s)
