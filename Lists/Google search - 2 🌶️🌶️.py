n = int(input())
l = []
ls = []
for i in range(n):
    s = input()
    l.append(s)
k = int(input())
for j in range(k):
    search = input()
    ls.append(search)
for o in l:
    for y in ls:
        if y in o:

