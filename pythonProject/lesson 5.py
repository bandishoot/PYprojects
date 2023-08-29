# def repl(str_1, str_, char, new_char):
#
#     if char in str_:
#         ind = str_.index(char, 1)
#         str_1 = str_[:ind] + str(new_char) + str_[str_.index(new_char):]
#     return str_1
#
#
# srt_1 = ''
# str_ = input('srtoka: ')
# char = input('symbol for change: ')
# new_char = input('new symbol: ')
#
# print(repl(str_1, str_, char, new_char))
#
# import re
#
# str_ = '''
#     id: 1234567
#     Granular convection is a phenomenon
#     output: success
#     where granular material subjected
# '''
#
# lst_ = re.findall(r'output:\s*[a-zA-Z ]+[?=\n]', str_)
#
# print(lst_)
#
# str_ = '''
#     128.0.70.0	128.0.70.255	256
# 157.167.127.0	157.167.127.255	256
# 178.170.132.0	178.170.135.255	1,024
# 178.170.147.0	178.170.147.255	256
# 178.170.160.0	178.170.163.255	1,024
# '''
#
# print(re.findall())

import random as rd


class Unit:
    def __init__(self, health, name, id_):
        self.health = health
        self.name = name
        self.id = id_

    def punch(self):
        self.health -= 10

        return self.health

    def lucky(self):
        rand = rd.randrange(30, 61, 10)

        if self.health == rand:
            print('lucky')
            self.health += 10

        return self.health


lst_name = ['dima', 'artem', 'misha']
lst = [Unit(100, i, rd.randint(100, 1000)) for i in lst_name]

print(lst[0].name)
print(lst[1].health)
print(lst[2].id)

while True:
    rand = rd.randrange(0, 3, 1)

    lst[rand].punch()
    lst[rand].lucky()

    print(lst[rand].name(), lst[rand].health())

    if lst[rand].health() == 0:
        print(lst[rand].name(), 'lost')
        break
