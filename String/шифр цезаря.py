sdvig = int(input())
kod = input()

for c in kod:
    if ord(c)-sdvig < 97:
        print(chr(ord(c)-sdvig + 26), end='')
    else:
        print(chr(ord(c)-sdvig), end='')
