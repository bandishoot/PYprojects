a, b = int(input()), int(input())
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0 and j != 2:
            continue
        else:
            print(i)
