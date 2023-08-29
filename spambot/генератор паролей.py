from random import *

up_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
letters = 'qwertyuiopasdfghjklzxcvbnm'
num = '1234567890'
symbols = '_@#$&*'
let = up_letters + letters

password = ''.join(sample(let, 8)) + choice(symbols) + ''.join(sample(num, 4))
print(password)
