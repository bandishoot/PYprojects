n = int(input())
l = []
s = 0
for i in range(n):
    a = int(input())
    s += a
    l.append(s)
    s = a
print(l[1:])
