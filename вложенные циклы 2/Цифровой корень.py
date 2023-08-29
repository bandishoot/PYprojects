n = int(input())
s1 = 0
s2 = 0
while n > 9:
    while n > 0:
        s1 += n % 10
        n //= 10
print(s1)z
