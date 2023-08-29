a, b, c = input(), input(), input()

if len(a) < len(b):
    b, a = a, b
if len(c) > len(b):
    c, b = b, c
if len(c) > len(a):
    c, a = a, c

print(c, a, sep='\n')
