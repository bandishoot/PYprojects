n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
search = input()
for i in l:
    if search in i.lower():
        print(i)
