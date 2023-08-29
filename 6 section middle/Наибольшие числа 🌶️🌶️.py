# put your python code here
n = int(input())
l1 = 0
l2 = 0
for i in range(n):
    x = int(input())
    if x > l1:
        l1 = x
    if l2 <= l1:
        l2 = x
print(l1, l2, sep='\n')
