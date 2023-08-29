n = int(input())
l = []
for i in range(n):
    x = input()
    if x not in l:
        l.append(x)
print(*l, sep='\n')
