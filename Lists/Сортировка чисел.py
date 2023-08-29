# put your python code here
s = input().split()
l = []
for i in s:
    l.append(int(i))
l.sort()
print(*l)
l.sort(reverse=True)
print(*l)

