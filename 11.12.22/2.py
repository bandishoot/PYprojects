a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b:
    ab = b
else:
    ab = a
if c > d:
    cd = d
else:
    cd = c
if cd < ab:
    print(cd)
else:
    print(ab)
