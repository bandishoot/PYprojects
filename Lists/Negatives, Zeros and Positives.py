n = int(input())
lower0 = []
upper0 = []
zero = []
for i in range(n):
    num = int(input())
    if num < 0:
        lower0.append(num)
    elif num > 0:
        upper0.append(num)
    else:
        zero.append(num)

