n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
l.remove(max(l))
l.remove(min(l))
print(l)
