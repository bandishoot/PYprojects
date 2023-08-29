n = int(input())
i = 0
while n // 25 >= 1:
    i += 1
    n -= 25
while n // 10 >= 1:
    i += 1
    n -= 10
while n // 5 >= 1:
    i += 1
    n -= 5
while n > 0:
    i += 1
    n -= 1
print(i)
